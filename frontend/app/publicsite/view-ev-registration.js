;(function (d) {
    'use strict';

    function getCsrfTokenFromCookie(){
        var cookies = d.cookie.split(';');
        for(var i = 0; i < cookies.length; i++) {
            var pair = cookies[i].split('=');
            if (pair[0].trim() == 'csrftoken') {
                return decodeURIComponent(pair[1].trim())
            }
        }
        return undefined;
    }

    function queryVisitorInformation(data, success, done) { // don't supported ie8-
        var xhr = new XMLHttpRequest();

        xhr.open('POST', '/queryvisitorinfo', true);
        xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');
        xhr.setRequestHeader('X-CSRFToken', getCsrfTokenFromCookie());
        xhr.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest');

        xhr.onload = function () {
            if (this.status != 200) return;

            success(JSON.parse(xhr.responseText));
        };
        xhr.onloadend = done;

        xhr.send(JSON.stringify(data));
    }

    var QUERY_FIELDS_PATTERN = 'div#visitor-form-query-fields > input';
    var AUTOFILL_FIELDS_PATTERN = 'div#visitor-form-autofill-fields > input';

    function processFields(pattern, func) {
        var fields = d.querySelectorAll(pattern);
        for(var i = 0; i < fields.length; i++) {
            func(fields[i]);
        }
    }

    function getQueryData() {
        var result = {};

        processFields(QUERY_FIELDS_PATTERN,
        function (field) {
            result[field.name] = field.value;
        });

        return result;
    }

    function setAutofillFieldsEnabled(enabled) {
        processFields(AUTOFILL_FIELDS_PATTERN,
        function (field) {
            field.disabled = !enabled;
        });
    }

    function fillData(data) {
        processFields(AUTOFILL_FIELDS_PATTERN,
        function (field) {
            field.value = data[field.name] || '';
        });
    }

    function onReady() {
        var emailInput = d.querySelectorAll('div#visitor-form-query-fields > input[type="email"]')[0];
        emailInput.onchange = function () {
            setAutofillFieldsEnabled(false);
            queryVisitorInformation(
                getQueryData(),
                fillData,
                function () {
                    setAutofillFieldsEnabled(true);
                }
            );
        };
    }

    /* dom ready impl, ie8- don't supported \ fuck old ie */

    var DOM_LOADED = 'DOMContentLoaded';
    d.addEventListener(DOM_LOADED, function (event) {
        d.removeEventListener(DOM_LOADED, onReady);
        onReady();
    });
})(document);