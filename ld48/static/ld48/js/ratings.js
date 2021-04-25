const starRatings = $(".star-rating");
const userRatingsJson = localStorage.getItem("ratings");
let userRatings = {};
if (userRatingsJson !== null) {
  userRatings = JSON.parse(userRatingsJson);
}

for (const starRating of starRatings) {
  const id = starRating.dataset.postId;
  if (id in userRatings) {
    starRating.classList.add("user-rated");
    for (let i = 1; i <= 5; i++) {
      const star = $(
        `.rating-star[data-post-id='${id}'][data-rating-star-value='${i}']`
      );
      if (i <= userRatings[id]) {
        star.removeClass("bi-star").addClass("bi-star-fill");
      } else {
        star.removeClass("bi-star-fill").addClass("bi-star");
      }
    }
  }
  $(`.rating-star[data-post-id='${id}']`).on("click", function (event) {
    if (!isLoggedIn() || starRating.dataset.postUsername == getUsername()) {
      return;
    }
    const value = event.target.dataset.ratingStarValue;
    let oldValue = null;
    if (id in userRatings) {
      oldValue = userRatings[id];
      if (value == oldValue) {
        return;
      }
    }
    let url = `/rate/?id=${id}&rating=${value}`;
    if (oldValue !== null) {
      url += `&old=${oldValue}`;
    }
    axios.post(url).then(function () {
      starRating.classList.add("user-rated");
      userRatings[id] = value;
      localStorage.setItem("ratings", JSON.stringify(userRatings));
      for (let i = 1; i <= 5; i++) {
        const star = $(
          `.rating-star[data-post-id='${id}'][data-rating-star-value='${i}']`
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
