import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '../views/common/LandingView.vue'
import PropertyCardView from '../views/tenant/PropertyCardView.vue'
import PropertyDetails from '../views/tenant/PropertyDetails.vue'
import TenantCardView from '../views/landlord/TenantCardView.vue'
import TenantDetails from '../views/landlord/TenantDetails.vue'
import LoginPageView from '../views/common/LoginPageView.vue'
import SignupPageView from '../views/common/SignupPageView.vue'
import TenantInspectionView from '../views/tenant/TenantInspectionView.vue'
import store from "../../store"

const routes = [
  {
    path: '/',
    name: 'landing',
    component: LandingView
  },
  {
    path: '/properties',
    name: 'available-properties',
    component: PropertyCardView,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/properties/:id',
    name: 'property-details',
    component: PropertyDetails,
    props: true,
    meta:{
      requiredLogin:true
    }
  },
  {
    path: '/tenants',
    name: 'prospective-tenants',
    component: TenantCardView,
    meta:{
      requiredLogin:true
    }
  },
  {
    path: '/tenants/:id',
    name: 'tenant-details',
    component: TenantDetails,
    props: true,
    meta:{
      requiredLogin:true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPageView,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupPageView,
  },
  {
    path: '/properties/inspections',
    name: 'tenant-inspect',
    component: TenantInspectionView,
    meta:{
      requiredLogin:true
    }
  },
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to,from,next) => {
  if(to.matched.some(record=>record.meta.requiredLogin) && !store.state.isAuthenticated){
    next('/login')
  }
  else{
    next()
  }
})

export default router
