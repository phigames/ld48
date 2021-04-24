const starRatings = $("input.star-rating");

for (const starRatingInput of starRatings) {
  const id = starRatingInput.dataset.ratingId;
  $(`.rating-star[data-rating-id='${id}']`).on("click", function (event) {
    const value = event.target.dataset.ratingStarValue;
    axios
      .post(`/ratings/?id=${id}&rating=${value}`)
      .then(function () {
        for (let i = 1; i < 6; i++) {
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
