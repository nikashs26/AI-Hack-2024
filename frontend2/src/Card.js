import React from "react";
import "./Card.css"

function Card({ title }) {
    return(
        <div className="card">
    <details>
        <summary>
            {title}
        </summary>
        <div>
            <a href={`/${title}`}> {title}</a>
        </div> 
    </details>
    </div>
    )
}

export default Card;