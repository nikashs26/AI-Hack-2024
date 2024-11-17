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
            <a href={`/page/${title}`}> {title}</a>
        </div> 
    </details>
    </div>
    )
}

export default Card;