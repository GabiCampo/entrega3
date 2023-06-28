const xhr = new XMLHttpRequest(); 
xhr.onload = function() { 
  const targettDiv = document.getElementById("targett-div"); 
  targettDiv.innerHTML = this.responseText; 
};
xhr.open("GET", "index_sin_registrar.html"); 
xhr.send(); 
