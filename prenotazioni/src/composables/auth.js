import {ref} from 'vue'

const token = ref(null);

export const useAuth = () => {
    const setToken = (newToken) => {
        token.value = newToken;
    };
    const getToken = () => {
        return token.value;
    };
    const isAuthenticated = () => {
        return token.value !== null;
    };
    const clearToken = () => {
        token.value = null;
    };

    return {
        setToken,
        getToken,
        isAuthenticated,
        clearToken
    };
}


