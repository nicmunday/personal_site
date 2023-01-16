// Open the Modal
function openCromerModal() {
  $("#cromerModal").css("display", "block")
}

// Close the Modal
function closeCromerModal() {
  $("#cromerModal").css("display", "none")
}

var cromerSlideIndex = 1;
showCromerSlides(cromerSlideIndex);

// Next/previous controls
function plusCromerSlides(n) {
  showCromerSlides(cromerSlideIndex += n);
}

// Thumbnail image controls
function currentCromerSlide(n) {
  showCromerSlides(cromerSlideIndex = n);
}

function showCromerSlides(n) {
  var i;
  var slides = $(".cromerSlides");
  if (n > slides.length) {cromerSlideIndex = 1}
  if (n < 1) {cromerSlideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
   }
  $(slides[cromerSlideIndex-1]).css("display", "block");
  $("#cromerCaption").text($(".cromerImage").eq([cromerSlideIndex-1]).attr("alt"));
  $("html").css("overflow-x", "hidden")
  $(document).keydown(function(event){
    if(event.which === 27){
      closeCromerModal();
    }
   });
}
