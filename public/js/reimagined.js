function showMenuItem(name, name2){
    $("#" + name).slideToggle();
    var classList = $("#" + name2).attr("class");
    var classs = classList.split(/\s+/);
    //alert(classs[0])
    for(i=0;i<classs.length; i++){
        if(classs[i] == "fa-angle-down"){
            $("#" + name2).removeClass("fa-angle-down");
            $("#" + name2).addClass("fa-angle-up");
        }
        else if(classs[i] == "fa-angle-up"){

            $("#" + name2).removeClass("fa-angle-up");
            $("#" + name2).addClass("fa-angle-down");
        }

    }
}

function showMainMenu(){
    $(".menuB").slideToggle();
    if($(".menuButton a").css("color") == "rgb(103, 122, 153)"){
        $(".menuButton a").css("color", "#fff");
    }else{
        $(".menuButton a").css("color", "#677a99");

    }
}