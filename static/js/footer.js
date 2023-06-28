const xhn = new XMLHttpRequest(); 
xhn.onload = function() { 
  const targetDiv = document.getElementById("target-div"); 
  targetDiv.innerHTML = this.responseText; 
};
xhn.open("GET", "footer.html"); 
xhn.send(); 
