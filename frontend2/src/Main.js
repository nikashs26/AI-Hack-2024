import React from "react";
import Card from "./Card";
import "./Main.css";
import lot from '/Users/nikashshanbhag/Documents/GitHub/AI-Hack-2024/frontend2/src/assets/parking-lot.png';
function HomePage()
{
    return(
        <div>
            <img class = "parking-lot" src={lot} alt="Lot" />
            <h1>Welcome to Peter Parks!</h1>
            



        
        

            <Card title="Castle Doom"/>
            <Card title="Dirty Docks"/>
            <Card title="Fatal Fields"/>
            <Card title="Greasy Grove"/>
            <Card title="Grand Glacier"/>
            <Card title="Haunted Hills"/>
            <Card title="Holly Hedges"/>
            <Card title="Junk Junction"/>
            <Card title="Lazy Lagoon"/>
            <Card title="Logjam Lotus"/>
            <Card title="Loot Lake"/>
            <Card title="Mjart Mall"/>
            <Card title="Pancake House"/>
            <Card title="Paradise Palms"/>
            <Card title="Pleasant Park"/>
            <Card title="Restored Reels"/>
            <Card title="Retail Row"/>
            <Card title="Salty Springs"/>
            <Card title="Tilted Towers"/>
            <Card title="Tomato Town"/>
            <Card title="Lazy Lagoon"/>

        </div>
    )
}

export default HomePage;