$(document).ready(function(){
  $('#dest').keyup(function(){
    var data = $("#add_trip").serialize() // capture all the data in the form in the variable data
    $.ajax({
      method: "POST", // we are using a post request here, but this could also be done with a get
      url: "welcome/../dest/",
      data: data
    })
    .done(function(res){
      $('#destMsg').html(res) // manipulate the dom when the response comes back
    })
  })
})

$(document).ready(function(){
  $('#desc').keyup(function(){
    var data = $("#add_trip").serialize() // capture all the data in the form in the variable data
    $.ajax({
      method: "POST", // we are using a post request here, but this could also be done with a get
      url: "welcome/../desc/",
      data: data
    })
    .done(function(res){
      $('#descMsg').html(res) // manipulate the dom when the response comes back
    })
  })
})

$(document).ready(function(){
  $('#start').change(function(){
    var data = $("#add_trip").serialize() // capture all the data in the form in the variable data
    $.ajax({
      method: "POST", // we are using a post request here, but this could also be done with a get
      url: "welcome/../start/",
      data: data
    })
    .done(function(res){
      $('#startMsg').html(res) // manipulate the dom when the response comes back
    })
  })
})

$(document).ready(function(){
  $('#end').change(function(){
    var data = $("#add_trip").serialize() // capture all the data in the form in the variable data
    $.ajax({
      method: "POST", // we are using a post request here, but this could also be done with a get
      url: "welcome/../end/",
      data: data
    })
    .done(function(res){
      $('#endMsg').html(res) // manipulate the dom when the response comes back
    })
  })
})
