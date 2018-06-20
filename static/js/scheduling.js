$(document).ready(function () {
  var csrftoken = getCookie('csrftoken');
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
  $('#search_available_sessions').click(function(event){
    alert("we in here # seraching");
    var subject = $('#id_subject').val();
    var date = $('#datepicker').data("DateTimePicker").date().format('YYYY-MM-DD');
    var time_start = $('#timestartpicker').data("DateTimePicker").date().format('HH:mm');
    var time_end  = $('#timeendpicker').data("DateTimePicker").date().format('HH:mm');

    alert(subject);
    alert(date);

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