import {Link} from "react-router-dom";
import "../static/navbar/navbar.css";
import { FaBars } from "react-icons/fa6";
import {useState} from "react";
const Navbar = () => {
    const [showLinks,setShowLinks] = useState(false)
    return (
        <div className="navbar">
            <ol className={showLinks?" show-links navbar-links":" hide-links navbar-links"}>
                <Link className="navbar-link" to="/">Home</Link>
                <Link className="navbar-link" to="/category/">Category</Link>
                <Link className="navbar-link" to="/settings/">Settings</Link>
                <Link className="navbar-link" >Cart</Link>
            </ol>
            <button className="navbar-bar-btn" onClick={()=> setShowLinks(!showLinks)}>
                <FaBars size="30px" />
            </button>
        </div>
    )
};export default Navbar ;