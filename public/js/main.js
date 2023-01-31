function toggleShowMore(linkName){
  if ($("#" + linkName).text() == "Show More"){
    $("#" + linkName).text("Show Less");
    $("#" + linksName + "2").text("Show Less");
  }
    else{
      $("#" + linkName).text("Show More");
      $("#" + linkName + "2").text("Show More");
    }
}

$("title").text("Nic Munday - Home")

