'use strict';

// Get location
var x = document.getElementById("demo");
let lat2=null;
let long2=null;
let tries = 0; // # of attempts to change the location
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  const lat = position.coords.latitude;
  const long = position.coords.longitude;
  ++tries;
  if (lat === lat2 && long === long2) {
    return;
  }
  x.innerHTML = "Location:<br>Lat: " + Math.round(lat*100000)/100000 +
  "&deg;<br>Long: " + Math.round(long*100000)/100000 + "&deg;";
  const velocity=getSpeed(lat,lat2,long,long2);
  if (lat2 !== null) {
    document.querySelector(".speed").innerHTML=`Speed: ${Math.round(velocity*100)/100} m/s`;
  }
  lat2=lat;
  long2=long;
  tries = 0;
}

function getSpeed(lat, lat2, long, long2){
	const r  = 6371;
	const latDistance = (lat-lat2)*Math.PI/180;
	const longDistance = (long-long2)*Math.PI/180;
	const area = Math.sin(latDistance/2)*Math.sin(latDistance/2)+Math.cos((lat)*Math.PI/180)*Math.cos((lat2)*Math.PI/180)*Math.sin(longDistance/2)*Math.sin(longDistance/2);
	const circum = 2* Math.atan(Math.sqrt(area), Math.sqrt(1-area));
	const distance = r*circum*1000;
	const totalDistance = Math.pow(distance,2);
	const speed = totalDistance/(3*tries);
	return speed;
}
setInterval(getLocation,3000);

// Get video feed
const videoElement = document.querySelector('video');
//const audioSelect = document.querySelector('select#audioSource');
const videoSelect = document.querySelector('select#videoSource');

navigator.mediaDevices.enumerateDevices()
  .then(gotDevices).then(getStream).catch(handleError);

//audioSelect.onchange = getStream;
videoSelect.onchange = getStream;

function gotDevices(deviceInfos) {
  for (let i = 0; i !== deviceInfos.length; ++i) {
    const deviceInfo = deviceInfos[i];
    const option = document.createElement('option');
    option.value = deviceInfo.deviceId;
    /*if (deviceInfo.kind === 'audioinput') {
      option.text = deviceInfo.label ||
        'microphone ' + (audioSelect.length + 1);
      audioSelect.appendChild(option);
    } else*/ if (deviceInfo.kind === 'videoinput') {
      option.text = deviceInfo.label || 'camera ' +
        (videoSelect.length + 1);
      videoSelect.appendChild(option);
    } else {
      console.log('Found another kind of device: ', deviceInfo);
    }
  }
}

function getStream() {
  if (window.stream) {
    window.stream.getTracks().forEach(function(track) {
      track.stop();
    });
  }

  const constraints = {
    /*audio: {
      deviceId: {exact: audioSelect.value}
    },*/
    video: {
      deviceId: {exact: videoSelect.value}
    }
  };

  navigator.mediaDevices.getUserMedia(constraints).
    then(gotStream).catch(handleError);
}

function gotStream(stream) {
  window.stream = stream; // make stream available to console
  videoElement.srcObject = stream;
}

function handleError(error) {
  console.error('Error: ', error);
}

// Get USB devices
/*navigator.usb.getDevices()
.then(devices => {
  document.querySelector('.controls').innerHTML += "Total devices: " + devices.length;
  devices.forEach(device => {
    document.querySelector('.controls').innerHTML += "Product name: " + device.productName + ", serial number " + device.serialNumber;
  });
});*/

// Get battery status
window.onload = function () {
	function updateBatteryStatus(battery) {
    const label = document.querySelector('#level');
		label.textContent = `${Math.round(battery.level*100)}%`;

    // Alert if low battery
		if(battery.level <= 0.2) {
		  alert('Low Battery');
      label.style.color = 'red';
		} else {
      label.style.color = 'white';
    }
	}

	navigator.getBattery().then(function(battery) {
		// Update the battery status initially when the promise resolves ...
		updateBatteryStatus(battery);

		// .. and for any subsequent updates.
		battery.onchargingchange = function () {
			updateBatteryStatus(battery);
		};

		battery.onlevelchange = function () {
			updateBatteryStatus(battery);
		};

		battery.ondischargingtimechange = function () {
			updateBatteryStatus(battery);
		};
	});
};
