$(document).ready(function() {
    $("#profile-avatar").click(function() {
        $("#user-menu").toggle();
    });

    $("#entries-menu").click(function() {
        $('#entries').css("display", "block");
        $('#overview').css("display", "none");
        $('#standings').css("display", "none");
        $("#overview-menu").removeClass("active");
        $("#standings-menu").removeClass("active");
        $("#entries-menu").addClass("active");
    });

    $("#overview-menu").click(function() {
        $('#entries').css("display", "none");
        $('#overview').css("display", "flex");
        $('#standings').css("display", "none");
        $("#entries-menu").removeClass("active");
        $("#standings-menu").removeClass("active");
        $("#overview-menu").addClass("active");
    });

    $("#standings-menu").click(function() {
        $('#entries').css("display", "none");
        $('#overview').css("display", "none");
        $('#standings').css("display", "block");
        $("#entries-menu").removeClass("active");
        $("#overview-menu").removeClass("active");
        $("#standings-menu").addClass("active");
    });

    
    $("#race-results-menu").click(function() {
        $('#race-results').css("display", "block");
        $('#qual-results').css("display", "none");
        $('#fastest-laps-results').css("display", "none");

        $("#qual-results-menu").removeClass("active");
        $("#fastest-laps-menu").removeClass("active");
        $("#race-results-menu").addClass("active");
    });

    $("#qual-results-menu").click(function() {
        $('#race-results').css("display", "none");
        $('#fastest-laps-results').css("display", "none");
        $('#qual-results').css("display", "block");
        
        $("#race-results-menu").removeClass("active");
        $("#fastest-laps-menu").removeClass("active");
        $("#qual-results-menu").addClass("active");
    });

    $("#fastest-laps-menu").click(function() {
        $('#race-results').css("display", "none");
        $('#qual-results').css("display", "none");
        $('#fastest-laps-results').css("display", "block");
        
        $("#race-results-menu").removeClass("active");
        $("#qual-results-menu").removeClass("active");
        $("#fastest-laps-menu").addClass("active");
    });


    $('.scroll-button-right').click(function(event) {
        event.preventDefault();
        $('#post-feed').animate({
            scrollLeft: "+=600px"
        }, "slow");
    });
    $('.scroll-button-left').click(function(event) {
        event.preventDefault();
        $('#post-feed').animate({
            scrollLeft: "-=600px"
        }, "slow");
    });
    $('#post-feed').scroll(function() {
        if ($(this).scrollLeft() >= 25) {
            $('#scroll-button-left').css('display', 'block')
        }
        if ($(this).scrollLeft() < 25) {
            $('#scroll-button-left').css('display', 'none')
        }
    });
});

$(document).click(function(event) {
    $target = $(event.target);
    if (!$target.closest('#user-menu').length && !$target.closest('#profile-avatar').length &&
        $('#user-menu').is(":visible")) {
        $('#user-menu').hide();
    }
});

function submitOnClick(formName){
    document.forms[formName].submit();
}