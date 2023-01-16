// Open the Modal
function openBrockModal() {
  $("#brockModal").css("display", "block")
}

// Close the Modal
function closeBrockModal() {
  $("#brockModal").css("display", "none")
}

var brockSlideIndex = 1;
showBrockSlides(brockSlideIndex);

// Next/previous controls
function plusBrockSlides(n) {
  showBrockSlides(brockSlideIndex += n);
}

// Thumbnail image controls
function currentBrockSlide(n) {
  showBrockSlides(brockSlideIndex = n);
}

function showBrockSlides(n) {
  var i;
  var slides = $(".brockSlides");
  if (n > slides.length) {brockSlideIndex = 1}
  if (n < 1) {brockSlideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
   }
  $(slides[brockSlideIndex-1]).css("display", "block");
  $("#brockCaption").text($(".brockImage").eq([brockSlideIndex-1]).attr("alt"));
  $("#brockCaption").css("overflow-x", "hidden")
  
   $(document).keydown(function(event){
    if(event.which === 27){
      closeBrockModal();
    }
   });

  // document.addEventListener('keydown', function(event) {
  //   if(event.key == "Escape"){
  //     closeBrockModal();
  //   }
  // });
}
