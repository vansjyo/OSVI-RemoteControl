$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

// Submit post on submit
$('#start_vid').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    start_vid();
});


function start_vid() {
    console.log("create post is working!") // sanity check
    console.log($('#start_vid').val())
    $.ajax({
        url: "start_vid",
        type: "POST",
        }
    ).delay
    sleep(3000);
    $('#iframe1').attr( 'src', function ( i, val ) { return val; });
};

$('#stop_vid').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")   // sanity check
    stop_vid();
});

function stop_vid() {
    console.log("create post is working!") // sanity check
    console.log($('#stop_vid').val())
    $.ajax({
        url: "stop_vid",
        type: "POST",
        }
    )
    sleep(3000);
    $('#iframe1').attr( 'src', function ( i, val ) { return val; });
    document.location.reload(1)
};

/*
$('#runcode').click(function(){
    console.log("Hello");
    start_vid();
});
*/
*/
/*
$('#runcode').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    var a = "{{ code }}";
    console.log(a)
//    runcode();
});
function runcode() {
    console.log("create post is working!") // sanity check
    var a = '{{code}}'
    console.log(a)
    $.ajax({
        url: "",
        type: "POST",
        data: {code : $('#runcode').val()}
        },
    );
};
*/