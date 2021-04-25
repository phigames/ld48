if (localStorage.getItem("username") === null) {
  console.log("username null");
  $("#register-container").css("display", "block");
}

function register() {
  event.preventDefault();
  const username = $("#uname").val();
  axios
    .get(`/check_username/${username}`)
    .then(function () {
      localStorage.setItem("username", username);
      location.reload();
    })
    .catch(function () {
      $("#register-error").text("Username already taken");
    });
}
