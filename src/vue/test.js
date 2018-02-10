const Vue = require('vue');
import json from '../result.json';

var staff = new Vue({
  el: '#main_page',
  data: {
    el: json,
  }
})
console.log(json.Size)
