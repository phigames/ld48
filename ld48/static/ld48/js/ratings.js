const starRatings = $(".star-rating");

for (const starRating of starRatings) {
  const id = starRating.dataset.ratingId;
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
