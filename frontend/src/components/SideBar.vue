<script>
import SidebarLink from './SideBarLink'
import { collapsed, toggleSidebar, sidebarWidth } from './state'
export default {
  props: {},
  components: { SidebarLink },
  setup() {
    return { collapsed, toggleSidebar, sidebarWidth }
  }
}
</script>

<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <h1>
      <span v-if="collapsed">
        <div></div>
      </span>
      <span v-else>Menu</span>
    </h1>
    <font-awesome-icon :icon="['fas', 'coffee']" />
    <SidebarLink icon="fa-solid fa-house" to="/">Landing</SidebarLink>
    <SidebarLink to="/login">Login</SidebarLink>
    <SidebarLink to="/signup">SignUp</SidebarLink>
    <SidebarLink to="/properties">Properties</SidebarLink>
    <SidebarLink to="/tenants">Tenants</SidebarLink>
    <SidebarLink to="/properties/inspections">Inspections</SidebarLink>


    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar"
    >
    <font-awesome-icon icon="fa-solid faUserSecret"></font-awesome-icon>
    </span>
  </div>
</template>

<style>
:root {
  --sidebar-bg-color: #2f855a;
  --sidebar-item-hover: #38a169;
  --sidebar-item-active: #276749;
}
</style>

<style scoped>
.sidebar {
  color: white;
  background-color: var(--sidebar-bg-color);
  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;
  transition: 0.3s ease;
  display: flex;
  flex-direction: column;
}
.sidebar h1 {
  height: 2.5em;
}
.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.75em;
  color: rgba(255, 255, 255, 0.7);
  transition: 0.2s linear;
}
.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}
</style>