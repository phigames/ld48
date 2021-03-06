if (!isLoggedIn()) {
  $("#hello-container").css("display", "block");
  $("#register-container").css("display", "block");
}

function register() {
  event.preventDefault();
  const username = $("#uname").val();
  axios
    .get(`/check_username/?username=${username}`)
    .then(function () {
      localStorage.setItem("username", username);
      location.reload();
    })
    .catch(function (error) {
      $("#register-error").text(error.response.data);
    });
}
