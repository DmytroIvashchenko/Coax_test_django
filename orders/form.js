$(document).ready(function () {
 $("#form").on('submit', function (){
   $.ajax({
     url: 'views.py',
     type: 'post',
     dataType: 'html',
     data: $(this).serialize(),
     success: function(data){
       $('#msg').html(data);
     }
   });
 });
});