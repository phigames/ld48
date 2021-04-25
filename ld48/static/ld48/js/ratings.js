const starRatings = $(".star-rating");
const userRatingsJson = localStorage.getItem("ratings");
let userRatings = {};
if (userRatingsJson !== null) {
  userRatings = JSON.parse(userRatingsJson);
}

for (const starRating of starRatings) {
  const id = starRating.dataset.ratingId;
  // TODO: check if already rated (in local storage), add user-rated class
  $(`.rating-star[data-rating-id='${id}']`).on("click", function (event) {
    const value = event.target.dataset.ratingStarValue;
    let oldValue = null;
    if (id in userRatings) {
      oldValue = userRatings[id];
      if (value == oldValue) {
        return;
      }
    }
    let url = `/ratings/?id=${id}&rating=${value}`;
    if (oldValue !== null) {
      url += `&old=${oldValue}`
    }
    axios.post(url).then(function () {
      starRating.classList.add("user-rated");
      userRatings[id] = value;
      localStorage.setItem("ratings", JSON.stringify(userRatings));
      for (let i = 1; i <= 5; i++) {
        const star = $(
          `.rating-star[data-rating-id='${id}'][data-rating-star-value='${i}']`
        );
        if (i <= value) {
          star.removeClass("bi-star").addClass("bi-star-fill");
        } else {
          star.removeClass("bi-star-fill").addClass("bi-star");
        }
      }
    });
  });
}
