const starRatings = $(".star-rating");

for (const starRating of starRatings) {
  const id = starRating.dataset.ratingId;
  // TODO: check if already rated (in local storage), add user-rated class
  $(`.rating-star[data-rating-id='${id}']`).on("click", function (event) {
    if (starRating.classList.contains('user-rated')) {
      // TODO: allow changing rating
      return;
    }
    const value = event.target.dataset.ratingStarValue;
    axios.post(`/ratings/?id=${id}&rating=${value}`).then(function () {
      starRating.classList.add("user-rated");
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
