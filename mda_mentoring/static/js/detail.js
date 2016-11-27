var eventInfo = {
  name: 'A meeting',
  details: 'This is an event description, these are some more words to fill it up.',

  eventLocation: {
    lat: -27.4698,
    lng: 153.0251,
    name: '123 Fake street, Brisbane, 4000'
  },

  attendees: [{
    name: 'Adam',
    role: 'Mentee'
  }, {
    name: 'Lennon',
    role: 'Mentee'
  }, {
    name: 'Martin',
    role: 'Mentee'
  }],

  invitable: [{
    name: 'Faye',
    role: 'Mentor'
  }]
};

var render = function (eventInfo) {
  var attendees = eventInfo.attendees;
  var invitable = eventInfo.invitable;
  var eventLocation = eventInfo.eventLocation;

  var map = new google.maps.Map(document.getElementById('map'), {
    disableDefaultUI: true,
    center: eventLocation,
    draggable: false,
    zoom: 9
  });

  var marker = new google.maps.Marker({
    position: eventLocation,
    map: map
  });

  var $attendeeList = document.querySelector('.list');

  $attendeeList.innerHTML += [
    '<div class="event-info">',
      '<h2>' + eventInfo.name + '</h2>',
      '<p>' + eventInfo.details + '</p>',
      '<span>' + attendees.length + ' attending</span><br />',
      '<span>' + eventLocation.name + '</span>',
    '</div>'
  ].join('');

  for (var i = 0; i < invitable.length; i++) {
    $attendeeList.innerHTML += [
      '<div class="invite-item">',
        '<div>',
          invitable[i].name + ' <span>' + invitable[i].role + '</span>',
          '<div class="invite-button">invite</div>',
        '</div>',
      '</div>',
    ].join('');
  }

  for (var i = 0; i < attendees.length; i++) {
    $attendeeList.innerHTML += [
      '<div>',
        '<div>',
          attendees[i].name + ' <span>' + attendees[i].role + '</span>',
        '</div>',
      '</div>',
    ].join('');
  }
};

render(eventInfo);
