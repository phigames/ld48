function selectWord(tokenIndex, word) {
  $(`#token-${tokenIndex}`).text(word);
}

function submit() {
  const words = [];
  for (const wordAlternativeSelect of $(".word-alternative-select")) {
    words.push(wordAlternativeSelect.innerText);
  }
  axios
    .post("/quote/", {
      words: words,
      username: "TODO USERNAME",
    })
    .then(function () {
      window.location.href = "/";
    });
}
