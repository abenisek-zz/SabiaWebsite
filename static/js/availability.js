$(document).ready(function () {
  alert(" inside the outside");
  var csrftoken = getCookie('csrftoken');
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
  $('#addSession').click(function(event){
    var date = $('#datepicker').data("DateTimePicker").date().format('YYYY-MM-DD');
    var time_start = $('#timestartpicker').data("DateTimePicker").date().format('HH:mm');
    var time_end  = $('#timeendpicker').data("DateTimePicker").date().format('HH:mm');

    console.log(date);
    $.ajax({
      type:"POST",
      url: "submit/",
      data: { CSRF: csrftoken, 'date': date, 'time_start': time_start, 'time_end' : time_end},
      success: function(data){
        window.location.href = "dashboard/";
      }

    });
  });
});

  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
