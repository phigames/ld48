function selectWord(tokenIndex, word) {
  $(`#token-${tokenIndex}`).text(word);
}

function submit() {
  const words = [];
  for (const wordAlternativeSelect of $(".word-alternative-select")) {
    words.push(wordAlternativeSelect.innerText);
  }
  const image = $(`#img_unsplash`).attr("src")
  axios
    .post("/new/", {
      words: words,
      username: localStorage.getItem("username"),
      image: image,
    })
    .then(function () {
      window.location.href = "/";
    });
}

window.onload = function () {
  axios
    .get("https://source.unsplash.com/500x500/?fitness,space,mountains,nature,inspirational")
    .then((response) => {
      $(`#img_unsplash`).attr("src", response.request.responseURL);
    })
}