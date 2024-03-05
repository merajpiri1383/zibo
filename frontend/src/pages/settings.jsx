import { Link ,Outlet } from "react-router-dom";
const Settings  =  () => {
    return (
        <div className="content">
            settings
            <Link to="/settings/add-product/">add product</Link>
            <Outlet />
        </div>
    )
};export default Settings ;