
// Making the season and episode img display in a separate div
var img_holder = document.getElementById("img_holder");
var season_name_img = document.getElementById("s_img").getElementsByTagName('img');

for(var i=0; i< season_name_img.length; i++){
    season_name_img[i].addEventListener('mouseover', full_image);
    
  }
  function full_image(){
    var ImageSRC = this.getAttribute('src');
    img_holder.innerHTML = "<img src="+ ImageSRC +" width='"+380+"', height='"+540+"' style='padding: 8px;' >"
  }

// ends here
