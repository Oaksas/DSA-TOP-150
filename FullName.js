function fullNameCorrector(names) {
  let correctedName = []
  for (i = 0; i < names.length; i++) {
    let name = names[i].toLowerCase()
    let [firstName, lastName] = name.split(" ")
    firstName = (firstName[0].toUpperCase() + firstName.slice(1)).trim()
    lastName = (lastName[0].toUpperCase() + lastName.slice(1)).trim()

    name = firstName + " " + lastName

    correctedName.push(name)

  }
  return correctedName

}
