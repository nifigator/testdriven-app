const randomstring = require('randomstring')

const username = randomstring.generate()
const email = `${username}@test.com`
const password = 'greaterthanten'

describe('Register', () => {

  it('should display the registration from', () => {
    cy
      .visit('/register')
      .get('h1').contains('Register')
      .get('form')

  })

  it('should allow a user to register', () => {
    cy
      .visit('/register')
      .get('input[name="username"]').type(username)
      .get('input[name="email"]').type(email)
      .get('input[name="password"]').type('test')
      .get('input[type="submit"]').click()

    // assert user is redirected to '/'
    // assert '/' is displayed properly
    cy.contains('All Users')
    cy.contains(username)
    cy.get('.navbar-burger').click()
    cy.get('.navbar-menu').within(() => {
      cy
        .get('.navbar-item').contains('User Status')
        .get('.navbar-item').contains('Log Out')
        .get('.navbar-item').contains('Log In').should('not.be.visible')
        .get('.navbar-item').contains('Register').should('not.be.visible')
    })
  })

  // it('should validate the password filed', () => {
  //   cy
  //     .visit('/register')
  //     .get('h1').containt('Register')
  //     .get('form')
  //     .get('input[disabled]')
  // })
})
