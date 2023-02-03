<template>
    <h2>Tenants Looking to Rent</h2>
    <div v-if="tenants">
        <div class="tenant-container">
            <div v-for="tenant in tenants" :key="tenant.id">
                <router-link :to="{name: 'tenant-details', params: { id: tenant.id}}">
                <div class="tenant">
                    <div class="image">
                        <img src="../../assets/logo.png" alt="">
                    </div>
                    <div class="details">
                        <h3>{{tenant.name}} ({{tenant.age}})</h3>
                        <sub>{{tenant.gender}}</sub>
                        <br>
                        <p>{{tenant.job}}</p>
                        <p>Preference: {{tenant.preference.type}}</p>
                    </div>
                </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
    export default{
        data(){
            return{
                tenants: []
            }
        },
        mounted(){
            fetch('http://localhost:3000/tenants')
            .then(res => res.json())
            .then(data => this.tenants = data)
            .catch(err => console.log(err.message))
        }
    }
</script>

<style scoped>

*{
    text-decoration: none;
}
.tenant-container{
    display: flex;
    align-content: space-around;
    padding: 10px;
    width:max-content;
    height: max-content;
    text-decoration: none;
    flex: 0 0 192px;
}
.tenant{
    text-decoration: none;
    border: 2px solid black;
    padding: 20px;
    margin: 15px;
    display: flex;
    align-content: space-between;

}
.tenant:hover{
    background:whitesmoke;
    border-radius: 10px;
    font-size: 1.05em;
}
.tenant a{
    text-decoration: none;
    color: black;
}
.image,.details{
    padding: 5px;
    text-decoration: none;
}
img{
    width: 100px;
    height: 100px;
}


</style>