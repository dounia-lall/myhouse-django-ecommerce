var counter = 2;
setInterval(function () {
  document.getElementById("radio" + counter).checked = true;
  counter++;
  if (counter > 9) {
    counter = 1;
  }
}, 5000);
