// var events = [{
//   title: 'event #1',
//   location: {
//     lat: -27.4698,
//     lng: 153.0251,
//     name: '123 Fake street, Brisbane, 4000'
//   },
//   attendees: 7
// }, {
//   title: 'event #2',
//   location: {
//     lat: -27.5998,
//     lng: 153.0281,
//     name: '123 Fake street, Brisbane, 4000'
//   },
//   attendees: 43
// }, {
//   title: 'event #3',
//   location: {
//     lat: -27.4698,
//     lng: 152.8251,
//     name: '123 Fake street, Brisbane, 4000'
//   },
//   attendees: 23
// }];

var render = function (position) {
  var map = new google.maps.Map(document.getElementById('map'), {
    disableDefaultUI: true,
    center: new window.google.maps.LatLng(
      position.coords.latitude,
      position.coords.longitude
    ),
    zoom: 9
  });

  var $eventList = document.querySelector('.list');

  for (var i = 0; i < data.length; i++) {
    var centerMarker = new window.RichMarker({
      content: '<div class="map-marker">' + data[i].attendees + '</div>',
      position: new window.google.maps.LatLng(
        data[i].lat,
        data[i].lng
      ),
      shadow: 'none',
      map: map
    });

    $eventList.innerHTML += [
      '<div>',
        '<div>',
          data[i].title + '<br /><span>' + data[i].name + '</span>',
        '</div>',
        '<div>',
          '<div>' + data[i].attendees + '</div>  attendees',
        '</div>',
      '</div>'
    ].join('');
  }
};

/*window.navigator
  ? window.navigator.geolocation.getCurrentPosition(render)
   default to Brisbane @ -27.4698,153.0251
  : render({ coords: { latitude: -27.4698, longitude: 153.0251 } });*/
