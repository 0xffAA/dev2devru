'use strict'

var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var bower = require('gulp-bower');
var uglify = require('gulp-uglify');
var bowerFiles = require('gulp-main-bower-files');
var filter = require('gulp-filter');

var paths = {
    publicsite: {
        input : {
            app: './app/publicsite/*.js',
            style: './style/publicsite/style.sass',
            img: ['./img/publicsite/*', './img/*', '!./img/publicsite/'],
            font: './font/*',
        },
        output : '../publicsite/static/'
    },
    libs: './libs/',
}

gulp.task('bower-update', function () {
    return bower({ cmd: 'update' });
});

gulp.task('libs-concat', ['bower-update'], function () {
    return gulp.src('./bower.json')
    .pipe(bowerFiles())
    .pipe(filter('**/*.js', { restore: true }))
    .pipe(concat('lib.js'))
    .pipe(uglify())
    .pipe(gulp.dest(paths.libs))
});

gulp.task('img-publicsite', function () {
    return gulp.src(paths.publicsite.input.img)
        .pipe(gulp.dest(paths.publicsite.output));
});

gulp.task('app-publicsite', function () {
    return gulp.src(paths.publicsite.input.app)
        .pipe(concat('app.js'))
        .pipe(gulp.dest(paths.publicsite.output));
});

gulp.task('style-publicsite', function () {
    return gulp.src(paths.publicsite.input.style)
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest(paths.publicsite.output));
});

gulp.task('font-publicsite', function () {
    return gulp.src(paths.publicsite.input.font)
        .pipe(gulp.dest(paths.publicsite.output));
});

gulp.task(
    'publicsite',
    ['font-publicsite', 'style-publicsite', 'img-publicsite', 'app-publicsite'],
    function () {
        return gulp.src(paths.libs + '*')
            .pipe(gulp.dest(paths.publicsite.output))
    }
);

gulp.task('watch', ['publicsite'], function() {
    gulp.watch(
        [
            paths.publicsite.input.app,
            paths.publicsite.input.style
        ],
        [
            'style-publicsite',
            'app-publicsite'
        ]);
});