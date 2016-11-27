var draw = function draw (id, data) {
  var goalCount = data.length;
  var sectionRad = Math.PI * 2 / goalCount;

  var svg = document.getElementById(id);
  svg.innerHTML = '';

  var width = 200;
  var height = 200;
  var radius = width / 2;

  for (var i = 0; i < goalCount; i++) {
    var x1 = radius + radius * (data[i].rating / 10) * Math.cos(2 * Math.PI * i / goalCount);
    var y1 = radius + radius * (data[i].rating / 10) * Math.sin(2 * Math.PI * i / goalCount);
    var x2 = radius + radius * (data[(i + 1) % data.length].rating / 10) * Math.cos(2 * Math.PI * (i + 1) / goalCount);
    var y2 = radius + radius * (data[(i + 1) % data.length].rating / 10) * Math.sin(2 * Math.PI * (i + 1) / goalCount);

    var points = radius + ',' + radius + ' ' + x1 + ',' + y1 + ' ' + x2 + ',' + y2;

    var poly = '<polygon points="' + points + '"></polygon>';
    svg.innerHTML += poly;
  }

  for (var i = 0; i < goalCount; i++) {
    var x = radius + radius * Math.cos(2 * Math.PI * i / goalCount);
    var y = radius + radius * Math.sin(2 * Math.PI * i / goalCount);

    var textPos = 0.9;

    var tx = radius + radius * textPos * Math.cos(2 * Math.PI * (i + 0.5) / goalCount);
    var ty = radius + radius * textPos * Math.sin(2 * Math.PI * (i + 0.5) / goalCount);

    var text = '<text x="' + tx + '" y="' + ty + '">' + data[i].rating + ' ' + data[i].name + '</text>';
    svg.innerHTML += text;

    var line = '<line x1="' + radius + '" x2="' + x + '" y1="' + radius + '" y2="' + y + '"></line>';
    svg.innerHTML += line;
  }
};

draw('graph', data);
