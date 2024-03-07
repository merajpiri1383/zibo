import { Link, Outlet } from "react-router-dom";
import "../static/settings/settings.css";
const Settings = () => {
    return (
        <div className="content">
            <div className="settings-links">
                <Link className="settings-link" to="/settings/create-product/">Create Product</Link>
                <Link className="settings-link" to="/settings/create-category/">Create Category</Link>
            </div>
            <Outlet />
        </div>
    )
}; export default Settings;