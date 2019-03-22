'use strict';

// Get location
var x = document.getElementById("demo");

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
  x.innerHTML = "Location:<br>Lat: " + Math.round(lat*100)/100 +
  "&deg;<br>Long: " + Math.round(long*100)/100 + "&deg;";
}

getLocation();

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

// Get battery status
window.onload = function () {
	function updateBatteryStatus(battery) {
		document.querySelector('#level').textContent = `${Math.round(battery.level*100)}%`;
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
