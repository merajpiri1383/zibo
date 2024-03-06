import { Link ,Outlet } from "react-router-dom";
const Settings  =  () => {
    return (
        <div className="content">
            settings
            <Link to="/settings/create-product/">Create Product</Link>
            <Link to="/settings/create-category/">Create Category</Link>
            <Outlet />
        </div>
    )
};export default Settings ;