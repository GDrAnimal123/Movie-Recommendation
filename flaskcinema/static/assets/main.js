// function call_api(api_name, params = {}) {
//     // console.log("Call_api is called...", params);
//     $.post({
//         url: Flask.url_for(api_name, params)
//     });
// }

(function() {
    var movieWell = {
        init: function() {
            this.cacheDom();
            this.bindEvents();
            this.render();
        },
        cacheDom: function() {
            this.$well = $('.post-content');
            this.$template = $('#book-well');
            // this.$dropdown = this.$well.find('.dropdown');
            // this.$ul = this.$dropdown.find('.dropdown-menu');
            // this.$a = this.$ul.find('a');
        },
        bindEvents: function() {
            // this.$a.on("click", this.rateMovie.bind(this));
        },
        render: function() {
            var bookWell = {
                imageUrl: "",
                movieName: "",
                userId: "",
                movieId: "",
                score: "No rating",
            }
            this.$well.html(Mustache.render(this.$template, bookWell))
        },
        // rateMovie: function(e) {
        //     var $this = $(e.target);

        //     var $rate_li = $this.closest('li');
        //     var $movie_input = $this.closest(this.$well).find('[name="movie_id"]');
        //     var $user_input = $this.closest(this.$well).find('[name="user_id"]');
        //     var $score_span = $this.closest(this.$well).find('.score');

        //     var movie_id = $movie_input.val();
        //     var user_id = $user_input.val();
        //     var score = parseInt($rate_li.index()) + 1;

        //     var rating = new Rating(movie_id, user_id, score)
        //     call_api("rate_movie", rating)

        //     $score_span.text(score);
        // }
    }

    movieWell.init();
})()





// $posts = $(".movies .post-content")

// $posts.find('img, #rate-icon').hover(function() {
//     $(this).parent().find('img').css('opacity', '0.4');
//     $(this).parent().find('#rate-icon').stop(true, true).show();;
// }, function() {
//     $(this).parent().find('img').css('opacity', '1.0');
//     $(this).parent().find('#rate-icon').stop(true, true).hide();;
// });

// $('[role="rating"]').on("click", function(event) {
//     var score = parseInt($(this).index()) + 1;
//     var rating = new Rating("movie_id=", "user_id=", score)
//     call_api("rate_movie", rating)
// });
