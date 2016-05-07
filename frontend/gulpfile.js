'use strict'

var gulp = require('gulp')
var sass = require('gulp-sass')

gulp.task('sass', function () {
    return gulp.src('./style/publicsite/style.sass')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('../publicsite/static/'));
});

gulp.task('watch', function() {
    gulp.watch('./style/publicsite/*.sass', ['sass']);
});