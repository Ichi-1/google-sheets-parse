
const ORDERS = 'http://localhost:8000/api/v1/orders/'
const CHART_DATA = 'http://localhost:8000/api/v1/chart/'
const TOTAL_COUNT = 'http://localhost:8000/api/v1/total-count/'

export default class OrderService {
    static async getOrders() {
        const response = await fetch(ORDERS, {
            method: "GET"
        })
        return response
    }

    static async getChartData() {
        const response = await fetch(CHART_DATA, {
            method: "GET"
        })
        return response
    }

    static async getTotalCount() {
        const response = await fetch(TOTAL_COUNT, {
            method: "GET"
        })
        return response
    }
}