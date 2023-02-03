<template>
<h1>Details</h1>
<div v-if="property">
    <div class="property-container">
        <div class="property-img">
            <img src="../../assets/logo.png" alt="">
        </div>
        <div class="property-title">
            <h2 class="title">{{ property.address }}</h2>
            <h3>{{property.price}}/week</h3>
            <p>{{property.bedrooms}} Bed, {{property.bathrooms}} Bath</p>
        </div>
        <div class="property-details">
            <div class="details">
                <p><strong>Property Summary: </strong>{{property.description}}</p>
            </div>
            <div class="preferences">
                <p><strong>Tenant Preference: </strong>{{property.preference.gender}}, {{property.preference.type}} </p>
            </div>
        </div>
    </div>
    <div class="property-images">

    </div>

    <div class="property-features">
        <PropertyFeatures :features="property.features"/>
    </div>
</div>
</template>

<script>
    import PropertyFeatures from '@/components/PropertyFeatures.vue';

    export default{
    props: ["id"],
    data() {
        return {
            property: null
        };
    },
    mounted() {
        fetch("http://localhost:3000/properties/" + this.id)
            .then(res => res.json())
            .then(data => this.property = data)
            .catch(err => console.log(err.message));
    },
    components: { PropertyFeatures }
}
    
</script>

<style scoped>
.property-img{
    border: 2px solid black;;
}
.property-container{
    display: flex;
    border: 2px solid black;
    padding: 100px;
    margin: 50px;
}
.property-features{
    border: 2px solid black;
    margin: 50px;
}
.property-title{
    position: relative;
    color: black;
    margin: 15px;
}
.property-details{
    padding: 50px;
}

</style>