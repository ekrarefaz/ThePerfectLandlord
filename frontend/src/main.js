import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'


/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUserSecret)

<<<<<<< HEAD

import axios from 'axios'

axios.defaults.baseURL = "http://localhost:8080"
=======
Vue.prototype.$http = axios;
>>>>>>> 79bc66c12efa5a81f414c7f84d087ba25064fc0b

createApp(App).use(router).component('font-awesome-icon', FontAwesomeIcon).mount('#app')
