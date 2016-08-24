'use strict'

var gulp = require('gulp')
var sass = require('gulp-sass')

gulp.task('img', function () {
    return gulp.src(['./img/publicsite/*', './img/*', '!./img/publicsite/'])
        .pipe(gulp.dest('../publicsite/static/'));
});


gulp.task('sass', function () {
    return gulp.src('./style/publicsite/style.sass')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('../publicsite/static/'));
});

gulp.task('font', function () {
    return gulp.src('./font/*')
        .pipe(gulp.dest('../publicsite/static/'));
});

gulp.task('publicsite', function () {
    return gulp.run('font', 'sass', 'img');
});

gulp.task('watch', function() {
    gulp.watch('./style/publicsite/*.sass', ['sass']);
});