function selectWord(tokenIndex, word) {
  $(`#token-${tokenIndex}`).text(word);
}

function submit() {
  const words = [];
  for (const wordAlternativeSelect of $(".word-alternative-select")) {
    words.push(wordAlternativeSelect.innerText);
  }
  const img = $(`#img_unsplash`).attr("src")
  console.log(img)
  axios
    .post("/quote/", {
      words: words,
      username: localStorage.getItem("username"),
      img: img,
    })
    .then(function () {
      window.location.href = "/";
    });
}

window.onload = function () {
  axios
    .get("https://source.unsplash.com/500x500/?fitness")
    .then((response) => {
      $(`#img_unsplash`).attr("src", response.request.responseURL);
    })
}