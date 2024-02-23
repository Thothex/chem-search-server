import  { FC } from "react";

const AuthButton: FC<{ buttonText: string }> = (props) => {
    const { buttonText } = props;

    return (
        <button>
            {buttonText}
        </button>
    );
};
export default AuthButton;
