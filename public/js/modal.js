// Open the Modal
var defaultSlideIndex = 0;

function openModal(modalName, n) {
  $("#" + modalName + "Modal").css("display", "block");
  showDefaultSlides(modalName, n);
}

// Close the Modal
function closeModal(modalName) {
  $("#" + modalName + "Modal").css("display", "none");
}

// Next/previous controls
function plusDefaultSlides(modalName, n) {
  showDefaultSlides(modalName, defaultSlideIndex += n);
}


function showDefaultSlides(modalName, n) {
  var i;
  var slides = $("." + modalName + "Slides");
  if (n > slides.length-1) {defaultSlideIndex = 0;}
  else if (n < 0) {defaultSlideIndex = slides.length-1;}
  else{defaultSlideIndex = n;}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
   }
  $(slides[defaultSlideIndex]).css("display", "block");
  
  $("#" + modalName + "Caption").text($("." + modalName + 
  "Image").eq(defaultSlideIndex).attr("alt"));

  $("html").css("overflow-x", "hidden")
  $(document).keydown(function(event){
    if(event.which === 27){
      closeModal(modalName);
    }
   });

}
