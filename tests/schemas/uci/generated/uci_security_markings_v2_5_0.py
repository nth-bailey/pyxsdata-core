from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from pyxsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "https://www.vdl.afrl.af.mil/programs/oam"


class AtomicEnergyMarkingsEnum(Enum):
    """
    CVEnumISMatomicEnergyMarkings Values.

    :cvar RD: RESTRICTED DATA
    :cvar RD_CNWDI: RD-CRITICAL NUCLEAR WEAPON DESIGN INFORMATION
    :cvar RD_SG_14: DOE Order 452.7 Restricted Data Sigma 14. Category
        of sensitive information, including bypass scenarios, concerning
        the vulnerability of nuclear weapons to a deliberate,
        unauthorized nuclear detonation or to the denial of authorized
        use.
    :cvar RD_SG_15: DOE Order 452.7 Restricted Data Sigma 15. Category
        of sensitive information concerning the design and function of
        nuclear weapon use control systems, features, and components.
    :cvar RD_SG_18: DOE Order 452.8 Restricted Data Sigma 18.Category of
        Nuclear Weapon Data including information that allows or
        significantly facilitates a nation or entity to fabricate a
        credible nuclear weapon or nuclear explosive device based on a
        proven, certified, or endorsed U.S. nuclear weapon or device.
    :cvar RD_SG_20: DOE Order 457.1A Restricted Data Sigma 20. Category
        of Nuclear Weapon Data that pertains to "crude, simple, or
        innovative" improvised nuclear device (IND) designs, concepts,
        and related manufacturing or processing pathways.
    :cvar FRD: FORMERLY RESTRICTED DATA
    :cvar FRD_SG_14: DOE Order 452.7 Formerly Restricted Data Sigma 14.
        Category of sensitive information, including bypass scenarios,
        concerning the vulnerability of nuclear weapons to a deliberate,
        unauthorized nuclear detonation or to the denial of authorized
        use.
    :cvar FRD_SG_15: DOE Order 452.7 Formerly Restricted Data Sigma 15.
        Category of sensitive information concerning the design and
        function of nuclear weapon use control systems, features, and
        components.
    :cvar FRD_SG_18: DOE Order 452.8 Formerly Restricted Data Sigma
        18.Category of Nuclear Weapon Data including information that
        allows or significantly facilitates a nation or entity to
        fabricate a credible nuclear weapon or nuclear explosive device
        based on a proven, certified, or endorsed U.S. nuclear weapon or
        device.
    :cvar FRD_SG_20: DOE Order 457.1A Formerly Restricted Data Sigma 20.
        Category of Nuclear Weapon Data that pertains to "crude, simple,
        or innovative" improvised nuclear device (IND) designs,
        concepts, and related manufacturing or processing pathways.
    :cvar DCNI: DoD CONTROLLED NUCLEAR INFORMATION
    :cvar UCNI: DoE CONTROLLED NUCLEAR INFORMATION
    :cvar TFNI: TRANSCLASSIFIED FOREIGN NUCLEAR INFORMATION
    """

    RD = "RD"
    RD_CNWDI = "RD_CNWDI"
    RD_SG_14 = "RD_SG_14"
    RD_SG_15 = "RD_SG_15"
    RD_SG_18 = "RD_SG_18"
    RD_SG_20 = "RD_SG_20"
    FRD = "FRD"
    FRD_SG_14 = "FRD_SG_14"
    FRD_SG_15 = "FRD_SG_15"
    FRD_SG_18 = "FRD_SG_18"
    FRD_SG_20 = "FRD_SG_20"
    DCNI = "DCNI"
    UCNI = "UCNI"
    TFNI = "TFNI"


class CuiBasicEnum(Enum):
    """
    (U) All currently valid CUI Basic markings from the National Archives.

    This enum is used by CUI_Basic. PERMISSIBLE VALUES The permissible
    values for this simple type are defined in the Controlled Value
    Enumeration: CVEnumISMCUIBasic.xml.

    :cvar ADPO: Administrative Proceedings. Adjudication of agency-
        related matters including, but not limited to, dispute
        resolution, settlements, and issuances of orders.
    :cvar AG: Agriculture. Information related to the agricultural
        operation, farming or conservation practices, or the actual land
        of an agricultural producer or landowner.
    :cvar ASYL: Asylee. Related to refugee applications and associated
        hearings to grant asylum to foreign nationals in the United
        States to be recognized as asylees.
    :cvar FSEC: Bank Secrecy. Information that is provided to the
        government pursuant to the Bank Secrecy Act, including but not
        limited to, suspicious activity reports (SAR), currency
        transaction reports (CTR), reports of international
        transportation of currency or monetary instruments (CMIR),
        reports of cash payment over $10,000 received in trade or
        business, and reports of foreign bank and financial accounts
        (FBAR). Reports filed under the Bank Secrecy Act (BSA), codified
        in relevant part at 31 U.S.C. § 5311 et seq, are specifically
        exempt from disclosure under the Freedom of Information Act,
        codified at 5 U.S.C. § 552, and also may not be disclosed under
        any State, local, tribal, or territorial "freedom of
        information," "open government," or similar law.  See 31 U.S.C.
        § 5319; 5 U.S.C. § 552(b)(3).  These reports (BSA Reports), are
        maintained in a system of records containing information
        compiled for law enforcement investigative purposes that has
        been exempted from the access provisions of the Privacy Act in
        accordance with 5 U.S.C. §§ 552a(j)(2) and (k)(2). BSA Reports
        may only be re-disseminated in strict accordance with guidelines
        established by the Financial Crimes Enforcement Network
        (FinCEN), the Treasury bureau that administers the BSA.
        Suspicious Activity Reports, one of the types of required
        reports filed under the BSA, are required to be kept
        confidential in accordance with 31 U.S.C. § 5318(g)(2) and
        implementing regulations. To the extent information falling
        under the purview of the BSA is collected, accessed, or used for
        any Federal tax administration purpose, it is also subject to
        the confidentiality provisions of the Internal Revenue Code,
        codified at 26 U.S.C. § 6103.
    :cvar BATT: Battered Spouse or Child. Related to information within
        applications and associated hearings provided by, or that could
        identify, a battered spouse or child of a US citizen or US
        permanent resident seeking independent protected status within
        the United States.
    :cvar CVI: Chemical-terrorism Vulnerability Information. In
        accordance with Section 550(c) of the Department of Homeland
        Security Appropriations Act of 2007, the following information,
        whether transmitted verbally, electronically, or in written
        form, shall constitute CVI, see (1) - (9).
    :cvar CVIC: Child Victim/Witness. Information pertaining to a minor
        who was a victim, witness, or potential witness to a criminal
        act.
    :cvar BARG: Collective Bargaining. Defining agencies' and
        representatives' duty to negotiate in good faith to include
        disclosure of certain labor relations training and guidance
        materials and limiting the issuance of certain subpoenas.
    :cvar CMPRS: Committed Person. Related to information concerning the
        mental condition of a person committed to a psychiatric
        facility.
    :cvar LCOMM: Communications. Related to the contents of any wire,
        oral, or electronic communication.
    :cvar COMPT: Comptroller General. Concerning the Officer of the
        United States Government who is charged with duties relating to
        fiscal affairs, including auditing, examining accounts, and
        reporting the financial status of the United States Government.
    :cvar DREC: Death Records.      Related to information contained
        within an official document issued by a public registry
        verifying that a person has died, with information such as the
        date and time of death, the cause of death, and the signature of
        the attending or examining physician.
    :cvar DCRIT: DoD Critical Infrastructure Security Information.
        Information that, if disclosed, would reveal vulnerabilities in
        the DoD critical infrastructure and, if exploited, would likely
        result in the significant disruption, destruction, or damage of
        or to DoD operations, property, or facilities, including
        information regarding the securing and safeguarding of
        explosives, hazardous chemicals, or pipelines, related to
        critical infrastructure or protected systems owned or operated
        on behalf of the DoD, including vulnerability assessments
        prepared by or on behalf of the DoD, explosives safety
        information (including storage and handling), and other site-
        specific information on or relating to installation security.
    :cvar XFER: Electronic Funds Transfer. Relating to the computer-
        based systems used to perform financial transactions
        electronically.
    :cvar EMGT: Emergency Management. Related to information concerning
        the continuity of executive branch operations during all-hazards
        emergencies or other situations that may disrupt normal
        operations.
    :cvar EXPT: Export Controlled. Unclassified information concerning
        certain items, commodities, technology, software, or other
        information whose export could reasonably be expected to
        adversely affect the United States national security and
        nonproliferation objectives. To include dual use items; items
        identified in export administration regulations, international
        traffic in arms regulations and the munitions list; license
        applications; and sensitive nuclear technology information.
    :cvar EXPTR: Export Controlled Research. Related to the systematic
        investigation into and study of materials and sources in order
        to establish facts and reach new conclusions.
    :cvar JURY: Federal Grand Jury. Material obtained pursuant to a
        federal grand jury subpoena, which includes (1) any reference to
        a specific sitting grand jury; (2) any documentation or data
        obtained by a grand jury subpoena if disclosure of such material
        tends to reveal what transpired before or at the direction of
        the federal grand jury; (3) documentation prepared specifically
        for the federal grand jury; and (4) transcripts or other
        recordings of testimony presented to the federal grand jury.
    :cvar FHFANPI: Federal Housing Finance Non-Public Information.
        Related to information that the Federal Housing Finance Agency
        (FHFA) has not made public that is created by, obtained by, or
        communicated to an FHFA employee in connection with the
        performance of official duties, regardless of who is in
        possession of the information, including confidential
        supervisory information. Confidential supervisory information
        includes FHFA reports of examination, inspection and visitation,
        confidential operating and condition reports, and any
        information derived from, related to, or contained in such
        reports, or gathered by FHFA in the course of any investigation,
        suspicious activity report, cease-and- desist order, civil money
        penalty enforcement order, suspension, removal or prohibition
        order, or other supervisory or enforcement orders or actions
        taken under the Federal Housing Enterprises Financial Safety and
        Soundness Act of 1992, and other conditions as set forth in 12
        CFR Part 1214.1.
    :cvar FSI: Financial Supervision Information. Related to information
        connected to an agency's responsibilities to supervise, examine,
        and evaluate a financial institution.
    :cvar CRIT: General Critical Infrastructure Information. Systems and
        assets, whether physical or virtual, so vital that the
        incapacity or destruction of such may have a debilitating impact
        on the security, economy, public health or safety, environment,
        or any combination of these matters, across any Federal, State,
        regional, territorial, or local jurisdiction.
    :cvar FNC: General Financial Information. Related to the duties,
        transactions, or otherwise falling under the purview of
        financial institutions or United States Government fiscal
        functions. Uses may include, but are not limited to, customer
        information held by a financial institution.
    :cvar INTEL: General Intelligence. Related to intelligence
        activities, sources, or methods.
    :cvar LEI: General Law Enforcement. Related to techniques and
        procedures for law enforcement operations, investigations,
        prosecutions, or enforcement actions.
    :cvar NUC: General Nuclear. Related to protection of information
        concerning nuclear reactors, materials, or security.
    :cvar PRVCY: General Privacy. Refers to personal information, or, in
        some cases, "personally identifiable information," as defined in
        OMB M-17-12, or "means of identification" as defined in 18 USC
        1028(d)(7).
    :cvar PROPIN: General Proprietary Business Information. Material and
        information relating to, or associated with, a company's
        products, business, or activities, including but not limited to
        financial information; data or statements; trade secrets;
        product research and development; existing and future product
        designs and performance specifications.
    :cvar GENETIC: Genetic Information. The term "genetic information"
        means, with respect to any individual, information about-- (i)
        such individual's genetic tests, (ii) the genetic tests of
        family members of such individual, and (iii) the manifestation
        of a disease or disorder in family members of such individual.
    :cvar HLTH: Health Information. As per 42 USC 1320d(4), "health
        information" means any information, whether oral or recorded in
        any form or medium, that (A) is created or received by a health
        care provider, health plan, public health authority, employer,
        life insurer, school or university, or health care
        clearinghouse; and (B) relates to the past, present, or future
        physical or mental health or condition of an individual, the
        provision of health care to an individual, or the past, present,
        or future payment for the provision of health care to an
        individual.
    :cvar CUI_PROVISIONAL_HSAI: Provisional - Homeland Security
        Agreement Information. Information DHS receives and is required
        to protect pursuant to an agreement with state, local, tribal,
        territorial, and private sector partners. DHS receives this
        information in furtherance of the missions of the Department,
        including but not limited to, support of the Fusion Center
        Initiative and activities for cyber information sharing
        consistent with the Cybersecurity Information Security Act.
    :cvar CUI_PROVISIONAL_HSEI: Provisional - Homeland Security
        Enforcement Information. Unclassified information of a sensitive
        nature lawfully created, possessed, or transmitted by DHS in
        furtherance of its immigration, customs, and other civil and
        criminal enforcement missions, the unauthorized disclosure of
        which could adversely impact the mission of the Department.
    :cvar INF: Informant. Related to the identity of a human source.
    :cvar ISVI: Information Systems Vulnerability Information. Related
        to information that if not protected, could result in adverse
        effects to information systems. Information system means a
        discrete set of information resources organized for the
        collection, processing, maintenance, use, sharing,
        dissemination, or disposition of information.
    :cvar CUI_PROVISIONAL_ISVIH: Provisional - Information Systems
        Vulnerability Information - Homeland. a. DHS information
        technology internal systems data revealing infrastructure used
        for servers, desktops, and networks; applications name, version
        and release; switching, router, and gateway information;
        interconnections and access methods; mission or business
        use/need.  Examples of information are systems inventories and
        enterprise architecture models.  Information pertaining to
        national security systems and eligible for classification under
        Executive Order 13526, will be classified as appropriate. b.
        Information regarding developing or current technology, the
        release of which could hinder the objectives of DHS, compromise
        a technological advantage or countermeasure, cause a denial of
        service, or provide an adversary with sufficient information to
        close, counterfeit, or circumvent a process or system.
    :cvar PRIIG: Inspector General Protected. Related to the identity of
        a person making a report to the Inspector General of any
        Executive agency.
    :cvar ID: Internal Data. Refers to a category of information that is
        not intended to be disseminated beyond CIA channels that
        involves intelligence activities, sources, or methods. This
        information may also relate to the CIA's organization,
        functions, names, official titles, salaries, or numbers of
        personnel.
    :cvar CUI_PROVISIONAL_IAIH: Provisional - International Agreement
        Information - Homeland. Information DHS receives and is required
        to protect pursuant to an information sharing agreement or
        arrangement with a foreign government, an international
        organization of governments or any element thereof, an
        international or foreign public or judicial body, or an
        international or foreign private or non-governmental
        organization.
    :cvar FINT: International Financial Institutions. Relating to
        entities that provide financial services for its clients or
        members, and were established (or chartered) by more than one
        country, and hence are subjects of international law.
    :cvar INVENT: Inventions. An invention is any art or process (way of
        doing or making things), machine, manufacture, design, or
        composition of matter, or any new and useful improvement
        thereof, or any variety of plant, which is or may be patentable
        under the patent laws of the United States, in which the federal
        government owns or may own a right, title, or interest.
    :cvar INV: Investigation. Related to information obtained during the
        course of a law enforcement investigation or action, civil or
        criminal.
    :cvar SURV: Investment Survey. Information reported to Treasury, the
        Federal Reserve Board of Governors, or the Federal Reserve Banks
        as part of the Treasury International Capital (TIC) data
        reporting system.
    :cvar JUV: Juvenile. Related to the identity of individual juvenile
        youths.
    :cvar PRIVILEGE: Legal Privilege. Per 12 USC 78x: The term
        "privilege" includes any work-product privilege, attorney-client
        privilege, governmental privilege, or other privilege recognized
        under Federal, State, or foreign law. Per 502(g): (1) "attorney-
        client privilege" means the protection that applicable law
        provides for confidential attorney-client communications; and
        (2) "work-product protection" means the protection that
        applicable law provides for tangible material (or its intangible
        equivalent) prepared in anticipation of litigation or for trial.
    :cvar LMI: Legislative Materials. Data related to Congress's
        legislative, investigatory or oversight responsibilities of the
        Executive branch of the Federal government.  This includes data
        related to proposed or pending legislation as well as inquiries
        submitted by Congress to Federal agencies, agency responses to
        those inquiries and any other information which, if disclosed,
        would reveal the nature and scope of Congressional inquiries.
    :cvar MERG: Mergers. Relating to methods by which corporations
        legally unify ownership of assets formerly subject to separate
        controls.
    :cvar MIL: Military Personnel Records. Any member or former member
        of the armed forces or affiliated organization of the Department
        of Defense.
    :cvar LNSL: National Security Letter.   Related to administrative
        orders sent to compel the recipients of the letters to provide
        information to federal investigators.
    :cvar NETW: Net Worth.  Related to the net worth of an individual
        and/or their affiliates in certain administrative proceedings.
    :cvar NNPI: Naval Nuclear Propulsion Information. Related to the
        safety of reactors and associated naval nuclear propulsion
        plants, and control of radiation and radioactivity associated
        with naval nuclear propulsion activities, including prescribing
        and enforcing standards and regulations for these areas as they
        affect the environment and the safety and health of workers,
        operators, and the general public.
    :cvar OPSEC: Critical information determined to give evidence of the
        planning and execution of sensitive (frequently classified)
        government activities after going through a formal systematic
        vetting process in accordance with National Security Decision
        Directive Number 298. This process identifies unclassified
        information that must be protected. It almost always results
        from an agency's official OPSEC program, or is otherwise
        commonly approved for use by the CUI Senior Agency Official.
    :cvar RECCOM: Nuclear Recommendation Material. Related to
        recommendations to the Secretary of Energy with respect to
        Department of Energy defense nuclear facilities as determined
        necessary to ensure adequate protection of public health and
        safety.
    :cvar SRI: Nuclear Security-Related Information. Related to
        information that could be useful, or could reasonably be
        expected to be useful, to a terrorist in a potential attack that
        does not qualify as Safeguards or classified information,
        including the exact location and quantities of radioactive
        material, certain detailed design drawings, information on
        nearby facilities, emergency planning information, and certain
        assessments of vulnerability and safety analyses.
    :cvar OCCMTO: Ocean Common Carrier and Marine Terminal Operator
        Agreements. Relating to agreements between or among ocean common
        carriers and marine terminal operators as referenced in 46 USC
        40301 and 40306.
    :cvar SERV: Ocean Common Carrier Service Contracts. Relating to an
        agreement for the provision of services filed with the Federal
        Maritime Commission as referenced in 46 USC 40502(b), 46 CFR
        530.4, and/or 46 CFR 531.4(a).
    :cvar CUI_PROVISIONAL_OSI: Provisional - Operations Security
        Information. Unclassified information that could constitute an
        indicator of U.S. Government intentions, capabilities,
        operations, or activities or otherwise threaten/compromise
        operations security.
    :cvar APP: Patent Applications. Application for patent filed under
        35 U.S.C. 111(a) that includes all types of patent applications
        (i.e., utility, design, plant, and reissue) except provisional
        applications. The nonprovisional application establishes the
        filing date and initiates the examination process. A
        nonprovisional utility patent application must include a
        specification, including a claim or claims; drawings, when
        necessary; an oath or declaration; and the prescribed filing
        fee.
    :cvar TRACE: Pen Register/Trap and Trace. Related to devices used to
        identify incoming and outgoing telephone numbers.
    :cvar RESD: Permanent Resident Status. Related to applications and
        associated hearings to grant permanent residency to foreign
        nationals living in the United States.
    :cvar PERS: Personnel Records. Related to the employees of federal
        agencies.
    :cvar CUI_PROVISIONAL_PSI: Provisional - Personnel Security
        Information.        Information that could result in physical
        risk to DHS personnel or other individuals that DHS is
        responsible for protecting.
    :cvar PEST: Pesticide Producer Survey. Related to the data gathered
        regarding the production of pesticides that specifies the non-
        disclosure of the identity and location of individual producers.
    :cvar PHYS: Physical Security. Related to protection of federal
        buildings, grounds or property.
    :cvar CUI_PROVISIONAL_PHYSH: Provisional - Physical Security -
        Homeland. Assessments or reports illustrating or disclosing
        facility infrastructure or security vulnerabilities related to
        the protection of federal buildings, grounds, or property, such
        as threat assessments, system security plans, contingency plans,
        risk management plans, business impact analysis studies, and
        certification and accreditation documentation.
    :cvar PRE: Presentence Report. A report, generally prepared to
        assist the court in determining the most appropriate sentence
        for a defendant. It can include an assessment of the nature and
        seriousness of the offense and should contain details
        summarizing the background information of the defendant and the
        crime.
    :cvar PRIOR: Prior Arrest. Information related to previous instances
        of law enforcement official's apprehension and formal processing
        of a suspect.
    :cvar CUI_PROVISIONAL_PRIVACY: Provisional - Privacy Information.
        Information referred to as Personally Identifiable Information
        (PII).  PII embodies information that can be used to distinguish
        or trace an individual's identity, either alone or when combined
        with other information that is linked or linkable to a specific
        individual.
    :cvar POST: Proprietary Postal. Concerning or related to the course
        of business of the United States Postal Service.
    :cvar LPROT: Protective Order.  Stipulation that certain information
        that would normally fall under discovery rules will not be
        disclosed for specifically stated reason.
    :cvar RAIL: Railroad Safety Analysis Records. Related to the
        establishment, implementation, or modification of a railroad
        safety risk reduction program or pilot program, if the record
        is: (1) Supplied to the Secretary (of Transportation) pursuant
        to that safety risk reduction program or pilot program; or (2)
        made available for inspection and copying by an officer,
        employee, or agent of the Secretary pursuant to that safety risk
        reduction program or pilot program.
    :cvar RTR: Retirement. Related to post-employment funding provided
        by an employer.
    :cvar RWRD: Reward. Related to the identity of a recipient of a
        reward.
    :cvar SAFE: SAFETY Act Information. Defined as "SAFETY Act
        Confidential Information" in 6 CFR Part 25, the regulations
        implementing the Support Anti-terrorism by Fostering Effective
        Technologies Act of 2002, SAFETY Act Information includes any
        and all information and data voluntarily submitted to the
        Department of Homeland Security under this part (including
        Applications, Pre-Applications, other forms, supporting
        documents and other materials relating to any of the foregoing,
        and responses to requests for additional information),
        including, but not limited to, inventions, devices, Technology,
        know-how, designs, copyrighted information, trade secrets,
        confidential business information, analyses, test and evaluation
        results, manuals, videotapes, contracts, letters, facsimile
        transmissions, electronic mail and other correspondence,
        financial information and projections, actuarial calculations,
        liability estimates, insurance quotations, and business and
        marketing plans.
    :cvar PSEC: Secrecy Orders. An order by the Commissioner of Patents
        that an invention be kept secret and to withhold the publication
        of an application or the grant of a patent due to national
        security concerns.
    :cvar CUI_PROVISIONAL_PII: Provisional - Sensitive Personally
        Identifiable Information. A subset of PII that, if lost,
        compromised or disclosed without authorization could result in
        substantial harm, embarrassment, inconvenience, or unfairness to
        an individual.  Some forms of PII are sensitive as stand-alone
        elements. a. Examples of stand-alone PII include: Social
        Security Numbers (SSN), driver's license or state identification
        number; Alien Registration Numbers; financial account number;
        and biometric identifiers such as fingerprint, voiceprint, or
        iris scan. b. Additional examples of SPII include any groupings
        of information that contain an individual's name or other unique
        identifier plus one or more of the following elements: Truncated
        SSN (such as last four digits) Date of birth (month, day, and
        year) Citizenship or immigration status Ethnic or religious
        affiliation Sexual orientation Criminal history Medical
        information System authentication information such as mother's
        maiden name, account passwords, or personal identification
        numbers c. Other PII may be "sensitive" depending on its
        context, such in as a list of employees and their performance
        rating(s) or an unlisted home address or phone number.  In
        contrast, a business card or public telephone directory of
        agency employees contains PII, but is not sensitive.
    :cvar SCV: Sex Crime Victim. Related to the identity of a victim of
        a sex offense.
    :cvar SBIZ: Small Business Research and Technology.     Relating to
        certain "Small Business Innovation Research Program" and "Small
        Business Technology Transfer Program" information in a
        government database, as referenced in 15 USC 638(k)(2).
    :cvar SSEL: Source Selection. Per FAR 2.101: any of the following
        information that is prepared for use by an agency for the
        purpose of evaluating a bid or proposal to enter into an agency
        procurement contract, if that information has not been
        previously made available to the public or disclosed publicly:
        (Items 1-10).
    :cvar STAT: Statistical Information. Refers to information collected
        by a Federal statistical agency, unit, or program for
        statistical purposes or used for statistical activities; under
        law, regulation, or Government-wide policy such 'Statistical'
        CUI requires: (1) protection from unauthorized disclosure; (2)
        special handling safeguards; and/or (3) prescribed limits on
        access or dissemination.
    :cvar ADJ: Status Adjustment. Related to applications for the
        adjustment of immigration status.
    :cvar STUD: Student Records. As per 20 USC 1232g, the Family
        Educational Rights and Privacy Act of 1974, an education record
        which is comprised of those records which are directly related
        to a student.
    :cvar CONREG: System for Award Management.      Relating to the
        primary United States Government system for contractor
        registration and awards.
    :cvar CONV: Tax Convention. Related to any-- (A) agreement entered
        into with the competent authority of one or more foreign
        governments pursuant to a tax convention, (B) application for
        relief under a tax convention, (C) background information
        related to such agreement or application, (D) document
        implementing such agreement, and (E) other information exchanged
        pursuant to a tax convention which is treated as confidential or
        secret under the tax convention. Tax convention information
        originating with the IRS generally retains its confidential
        status even when it resides with agencies other than the IRS.
    :cvar TAI: Taxpayer Advocate Information. A local taxpayer advocate
        (LTA) has the discretion to not disclose to the IRS contact
        with, or information provided by, a taxpayer.  Such discretion
        may result in declinations of requests for information by IRS
        personnel including cases involving criminal tax investigations
        or those where the failure to provide information to the IRS
        would be beneficial to the taxpayer but to the detriment of the
        IRS.  Such discretion does not extend to cases where the LTA
        believes a taxpayer is using the Taxpayer Advocate's office to
        perpetuate a fraud on the government or in cases where the
        information is sought in litigation.
    :cvar PROT: Temporary Protected Status. Related to findings that
        conditions in a given country pose a danger to personal safety
        due to ongoing armed conflict or an environmental disaster and
        persons should receive special temporary status to remain in the
        United States.
    :cvar LSCRN: Terrorist Screening. Related to information gathering
        and analysis concerning possible threats or acts of a
        destructive nature.
    :cvar DCNI: Unclassified Controlled Nuclear Information - Defense.
        Relating to Department of Defense special nuclear material
        (SNM), equipment, and facilities, as defined by 32 CFR 223.
    :cvar UCNI: Unclassified Controlled Nuclear Information - Energy.
        Relating to certain design and security information concerning
        nuclear facilities, materials, and weapons, specific to the
        Department of Energy.
    :cvar LVIC: Victim. Information requiring protection of the name or
        other details that may identify one who was the victim of a
        crime.
    :cvar IVIC: Victims of Human Trafficking. Related to identifiable
        information of persons who have been victims of human
        trafficking and their family members.
    :cvar VISA: Visas. Related to applications or permits to enter the
        United States.
    :cvar WATER: Water Assessments. Vulnerability Assessments on the
        risks and security of public drinking water systems, to include,
        but not be limited to, a review of pipes and constructed
        conveyances, physical barriers, water collection, pretreatment,
        treatment, storage and distribution facilities, electronic,
        computer or other automated systems which are utilized by the
        public water system, the use, storage, or handling of various
        chemicals, and the operation and maintenance of such system.
    :cvar WHSTL: Whistleblower Identity. Identity of anyone providing
        information relating to a legal violation or illicit or unsafe
        activity, including information provided by a whistleblower
        which could reasonably be expected to reveal the identity of a
        whistleblower.
    :cvar WIT: Witness Protection. Information related to the secretive
        details associated with one who has testified or may testify
        under circumstances that require secrecy of that individual and
        details pertaining to that person.
    """

    ADPO = "ADPO"
    AG = "AG"
    ASYL = "ASYL"
    FSEC = "FSEC"
    BATT = "BATT"
    CVI = "CVI"
    CVIC = "CVIC"
    BARG = "BARG"
    CMPRS = "CMPRS"
    LCOMM = "LCOMM"
    COMPT = "COMPT"
    DREC = "DREC"
    DCRIT = "DCRIT"
    XFER = "XFER"
    EMGT = "EMGT"
    EXPT = "EXPT"
    EXPTR = "EXPTR"
    JURY = "JURY"
    FHFANPI = "FHFANPI"
    FSI = "FSI"
    CRIT = "CRIT"
    FNC = "FNC"
    INTEL = "INTEL"
    LEI = "LEI"
    NUC = "NUC"
    PRVCY = "PRVCY"
    PROPIN = "PROPIN"
    GENETIC = "GENETIC"
    HLTH = "HLTH"
    CUI_PROVISIONAL_HSAI = "CUI_PROVISIONAL_HSAI"
    CUI_PROVISIONAL_HSEI = "CUI_PROVISIONAL_HSEI"
    INF = "INF"
    ISVI = "ISVI"
    CUI_PROVISIONAL_ISVIH = "CUI_PROVISIONAL_ISVIH"
    PRIIG = "PRIIG"
    ID = "ID"
    CUI_PROVISIONAL_IAIH = "CUI_PROVISIONAL_IAIH"
    FINT = "FINT"
    INVENT = "INVENT"
    INV = "INV"
    SURV = "SURV"
    JUV = "JUV"
    PRIVILEGE = "PRIVILEGE"
    LMI = "LMI"
    MERG = "MERG"
    MIL = "MIL"
    LNSL = "LNSL"
    NETW = "NETW"
    NNPI = "NNPI"
    OPSEC = "OPSEC"
    RECCOM = "RECCOM"
    SRI = "SRI"
    OCCMTO = "OCCMTO"
    SERV = "SERV"
    CUI_PROVISIONAL_OSI = "CUI_PROVISIONAL_OSI"
    APP = "APP"
    TRACE = "TRACE"
    RESD = "RESD"
    PERS = "PERS"
    CUI_PROVISIONAL_PSI = "CUI_PROVISIONAL_PSI"
    PEST = "PEST"
    PHYS = "PHYS"
    CUI_PROVISIONAL_PHYSH = "CUI_PROVISIONAL_PHYSH"
    PRE = "PRE"
    PRIOR = "PRIOR"
    CUI_PROVISIONAL_PRIVACY = "CUI_PROVISIONAL_PRIVACY"
    POST = "POST"
    LPROT = "LPROT"
    RAIL = "RAIL"
    RTR = "RTR"
    RWRD = "RWRD"
    SAFE = "SAFE"
    PSEC = "PSEC"
    CUI_PROVISIONAL_PII = "CUI_PROVISIONAL_PII"
    SCV = "SCV"
    SBIZ = "SBIZ"
    SSEL = "SSEL"
    STAT = "STAT"
    ADJ = "ADJ"
    STUD = "STUD"
    CONREG = "CONREG"
    CONV = "CONV"
    TAI = "TAI"
    PROT = "PROT"
    LSCRN = "LSCRN"
    DCNI = "DCNI"
    UCNI = "UCNI"
    LVIC = "LVIC"
    IVIC = "IVIC"
    VISA = "VISA"
    WATER = "WATER"
    WHSTL = "WHSTL"
    WIT = "WIT"


class CuiSpecifiedEnum(Enum):
    """
    (U) All currently valid CUI Specified markings from the National
    Archives.

    This enum is used by CUI_Specified. PERMISSIBLE VALUES The permissible
    values for this simple type are defined in the Controlled Value
    Enumeration: CVEnumISMCUISpecified.xml.

    :cvar AIV: Accident Investigation. Related to information obtained
        during the course of an accident or incident investigation.
        Including but not limited to information related to wreckage,
        records, mail, or cargo.
    :cvar ADPO: Administrative Proceedings. Adjudication of agency-
        related matters including, but not limited to, dispute
        resolution, settlements, and issuances of orders.
    :cvar CRITAN: Ammonium Nitrate. Related to registration information
        of those who own and operate ammonium nitrate facilities,
        purchasers of ammonium nitrate, and the regulation of sales and
        transfers of ammonium nitrate.
    :cvar ARCHR: Archaelogical Resources. Related to information about
        the nature and location of any archaeological resource for which
        the excavation or removal requires a permit or other permission.
    :cvar FSEC: Bank Secrecy. Information that is provided to the
        government pursuant to the  Bank Secrecy Act, including but not
        limited to, suspicious activity reports (SAR), currency
        transaction reports (CTR), reports of international
        transportation of currency or monetary instruments (CMIR),
        reports of cash payment over $10,000 received in trade or
        business, and reports of foreign bank and financial accounts
        (FBAR). Reports filed under the Bank Secrecy Act (BSA), codified
        in relevant part at 31 U.S.C. § 5311 et seq, are specifically
        exempt from disclosure under the Freedom of Information Act,
        codified at 5 U.S.C. § 552, and also may not be disclosed under
        any State, local, tribal, or territorial "freedom of
        information," "open government," or similar law.  See 31 U.S.C.
        § 5319; 5 U.S.C. § 552(b)(3).  These reports (BSA Reports), are
        maintained in a system of records containing information
        compiled for law enforcement investigative purposes that has
        been exempted from the access provisions of the Privacy Act in
        accordance with 5 U.S.C. §§ 552a(j)(2) and (k)(2). BSA Reports
        may only be re-disseminated in strict accordance with guidelines
        established by the Financial Crimes Enforcement Network
        (FinCEN), the Treasury bureau that administers the BSA.
        Suspicious Activity Reports, one of the types of required
        reports filed under the BSA, are required to be kept
        confidential in accordance with 31 U.S.C. § 5318(g)(2) and
        implementing regulations. To the extent information falling
        under the purview of the BSA is collected, accessed, or used for
        any Federal tax administration purpose, it is also subject to
        the confidentiality provisions of the Internal Revenue Code,
        codified at 26 U.S.C. § 6103.
    :cvar BUDG: Budget. Related to information concerning the federal
        budget, including authorizations and estimates of income and
        expenditures.
    :cvar FUND: Campaign Funds. Related to information obtained in
        connection to an investigation into campaign finance and
        disclosure laws. Usage may include but is not limited to
        notification or investigation pertaining to financial support of
        a candidate for election.
    :cvar CVI: Chemical-terrorism Vulnerability Information. In
        accordance with Section 550(c) of the Department of Homeland
        Security Appropriations Act of 2007, the following information,
        whether transmitted verbally, electronically, or in written
        form, shall constitute CVI, see (1) - (9).
    :cvar CHLD: Child Pornography. From 18 USC 2256(8) "child
        pornography" means any visual depiction, including any
        photograph, film, video, picture, or computer or computer-
        generated image or picture, whether made or produced by
        electronic, mechanical, or other means, of sexually explicit
        conduct, where— (A) the production of such visual depiction
        involves the use of a minor engaging in sexually explicit
        conduct; (B) such visual depiction is a digital image, computer
        image, or computer-generated image that is, or is
        indistinguishable from, that of a minor engaging in sexually
        explicit conduct; or (C) such visual depiction has been created,
        adapted, or modified to appear that an identifiable minor is
        engaging in sexually explicit conduct
    :cvar CCI: Consumer Complaint Information. Related to information
        concerning consumer complaints or inquiries concerning financial
        institutions or consumer financial products and services, and
        responses to them.
    :cvar CONTRACT: Contract Use. Stipulations for a contractor to meet
        before material may be used in performance of certain contracts.
    :cvar SUB: Controlled Substances. Information obtained by the Drug
        Enforcement Administration (DEA) or in DEA investigative reports
        related to controlled substances.
    :cvar CTI: Controlled Technical Information. Controlled Technical
        Information means technical information with military or space
        application that is subject to controls on the access, use,
        reproduction, modification, performance, display, release,
        disclosure, or dissemination. Controlled technical information
        is to be marked with one of the distribution statements B
        through F, in accordance with Department of Defense Instruction
        5230.24, "Distribution Statements of Technical Documents." The
        term does not include information that is lawfully publicly
        available without restrictions. "Technical Information" means
        technical data or computer software, as those terms are defined
        in Defense Federal Acquisition Regulation Supplement clause
        252.227-7013, "Rights in Technical Data - Noncommercial Items"
        (48 CFR 252.227-7013). Examples of technical information include
        research and engineering data, engineering drawings, and
        associated lists, specifications, standards, process sheets,
        manuals, technical reports, technical orders, catalog-item
        identifications, data sets, studies and analyses and related
        information, and computer software executable code and source
        code.
    :cvar CHRI: Criminal History Records Information. Related to
        information collected by criminal justice agencies on
        individuals consisting of identifiable descriptions and
        notations of arrests, detentions, indictments, informations, or
        other formal criminal charges, and any disposition arising
        therefrom, including acquittal, sentencing, correctional
        supervision, and release.
    :cvar CEII: Critical Energy Infrastructure Information. Critical
        energy infrastructure information means specific engineering,
        vulnerability, or detailed design information about proposed or
        existing critical infrastructure that: (i) Relates details about
        the production, generation, transportation, transmission, or
        distribution of energy; (ii) Could be useful to a person in
        planning an attack on critical infrastructure;... and (iii) Does
        not simply give the general location of the critical
        infrastructure.
    :cvar LDNA: DNA. Related to hereditary material in humans that is
        used for law enforcement purposes.
    :cvar EXPT: Export Controlled. Unclassified information concerning
        certain items, commodities, technology, software, or other
        information whose export could reasonably be expected to
        adversely affect the United States national security and
        nonproliferation objectives. To include dual use items; items
        identified in export administration regulations, international
        traffic in arms regulations and the munitions list; license
        applications; and sensitive nuclear technology information.
    :cvar JURY: Federal Grand Jury. Material obtained pursuant to a
        federal grand jury subpoena, which includes (1) any reference to
        a specific sitting grand jury; (2) any documentation or data
        obtained by a grand jury subpoena if disclosure of such material
        tends to reveal what transpired before or at the direction of
        the federal grand jury; (3) documentation prepared specifically
        for the federal grand jury; and (4) transcripts or other
        recordings of testimony presented to the federal grand jury.
    :cvar TAX: Federal Taxpayer Information. Related to returns and
        return information which are submitted, gathered or generated in
        conjunction with taxpayers' responsibilities to comply with
        federal tax provisions in the United States Code. "Returns"
        includes information that is provided to the government pursuant
        to Title 26, including tax or information returns, declarations
        of estimated tax or claims for refund.  "Return information"
        includes a taxpayer's identity, the nature, source or amount of
        income or any information received by, recorded by, prepared by
        or furnished to Internal Revenue Service relevant to the
        determination of tax liability including whether the taxpayer is
        the subject of investigation.  This protection extends to such
        items as medical, financial and other personal information
        submitted to the IRS by taxpayers.  Standards (typically
        tolerances, audit criteria and law enforcement techniques)
        related to the selection of returns for examination should only
        be disclosed to the extent their disclosure would not impair
        assessment, collection or enforcement under the internal revenue
        laws.  Tax data originating with the IRS generally retains its
        confidential status even when it resides with agencies other
        than the IRS.
    :cvar FISA: Foreign Intelligence Surveillance Act. Related to
        unclassified and declassified information that is collected from
        unconsenting individuals under the authority of the Foreign
        Intelligence Surveillance Act (FISA).
    :cvar FISAB: Foreign Intelligence Surveillance Act Business Records.
        Related to books, records, papers, documents, and other items
        produced for an investigation to obtain foreign intelligence
        information.
    :cvar FNC: General Financial Information. Related to the duties,
        transactions, or otherwise falling under the purview of
        financial institutions or United States Government fiscal
        functions. Uses may include, but are not limited to, customer
        information held by a financial institution.
    :cvar INTEL: General Intelligence. Related to intelligence
        activities, sources, or methods.
    :cvar NUC: General Nuclear. Related to protection of information
        concerning nuclear reactors, materials, or security.
    :cvar PRVCY: General Privacy. Refers to personal information, or, in
        some cases, "personally identifiable information," as defined in
        OMB M-17-12, or "means of identification" as defined in 18 USC
        1028(d)(7).
    :cvar PROCURE: General Procurement and Acquisition. Material and
        information relating to, or associated with, the acquisition and
        procurement of goods and services, including but not limited to,
        cost or pricing data, contract information, indirect costs and
        direct labor rates.
    :cvar PROPIN: General Proprietary Business Information. Material and
        information relating to, or associated with, a company's
        products, business, or activities, including but not limited to
        financial information; data or statements; trade secrets;
        product research and development; existing and future product
        designs and performance specifications.
    :cvar GENETIC: Genetic Information. The term "genetic information"
        means, with respect to any individual, information about-- (i)
        such individual's genetic tests, (ii) the genetic tests of
        family members of such individual, and (iii) the manifestation
        of a disease or disorder in family members of such individual.
    :cvar GEO: Geodetic Product Information. Related to imagery, imagery
        intelligence, or geospatial information.
    :cvar HLTH: Health Information. As per 42 USC 1320d(4), "health
        information" means any information, whether oral or recorded in
        any form or medium, that (A) is created or received by a health
        care provider, health plan, public health authority, employer,
        life insurer, school or university, or health care
        clearinghouse; and (B) relates to the past, present, or future
        physical or mental health or condition of an individual, the
        provision of health care to an individual, or the past, present,
        or future payment for the provision of health care to an
        individual.
    :cvar HISTP: Historic Properties. Related to the location,
        character, or ownership of historic property.
    :cvar INF: Informant. Related to the identity of a human source.
    :cvar PRIIG: Inspector General Protected. Related to the identity of
        a person making a report to the Inspector General of any
        Executive agency.
    :cvar IFNC: Intelligence Financial Records. Related to financial
        records obtained for intelligence or counterintelligence
        activity, investigation, or analysis.
    :cvar ID: Internal Data. Refers to a category of information that is
        not intended to be disseminated beyond CIA channels that
        involves intelligence activities, sources, or methods. This
        information may also relate to the CIA's organization,
        functions, names, official titles, salaries, or numbers of
        personnel.
    :cvar INTL: International Agreement Information. Information
        provided by, otherwise made available by, or produced in
        cooperation with, a foreign government or international
        organization that requires protection pursuant to an existing
        treaty, agreement, bilateral exchange or other obligation under
        the requirements stipulated in 10 USC 130c(b), when not subject
        to classification under Executive Order 13526. Title 10 USC
        130c(b) may exempt this class of foreign government information
        from the safeguard provisions otherwise required by Executive
        Order 13526. Per Title 10 USC 130c(h) the following national
        security officials are the only ones defined by statute as able
        to determine such information requires control: (A) The
        Secretary of Defense, with respect to information of concern to
        the Department of Defense. (B) The Secretary of Homeland
        Security, with respect to information of concern to the Coast
        Guard, as determined by the Secretary, but only while the Coast
        Guard is not operating as a service in the Navy. (C) The
        Secretary of Energy, with respect to information concerning the
        national security programs of the Department of Energy, as
        determined by the Secretary.
    :cvar INV: Investigation. Related to information obtained during the
        course of a law enforcement investigation or action, civil or
        criminal.
    :cvar LFNC: Law Enforcement Financial Records. Related to financial
        records obtained for law enforcement purposes.
    :cvar NPSR: National Park System Resources. Related to information
        concerning the nature and specific location of a National Park
        System resource that is endangered, threatened, rare, or
        commercially valuable, of mineral or paleontological objects
        within System units, or of objects of cultural patrimony within
        System units.
    :cvar NNPI: Naval Nuclear Propulsion Information. Related to the
        safety of reactors and associated naval nuclear propulsion
        plants, and control of radiation and radioactivity associated
        with naval nuclear propulsion activities, including prescribing
        and enforcing standards and regulations for these areas as they
        affect the environment and the safety and health of workers,
        operators, and the general public.
    :cvar SRI: Nuclear Security-Related Information. Related to
        information that could be useful, or could reasonably be
        expected to be useful, to a terrorist in a potential attack that
        does not qualify as Safeguards or classified information,
        including the exact location and quantities of radioactive
        material, certain detailed design drawings, information on
        nearby facilities, emergency planning information, and certain
        assessments of vulnerability and safety analyses.
    :cvar PERS: Personnel Records. Related to the employees of federal
        agencies.
    :cvar MFC: Proprietary Manufacturer. Relating to the production of a
        consumer product to include that of a private labeler.
    :cvar PCII: Protected Critical Infrastructure Information. As
        defined by 6 USC 131-134, and 6 CFR 29, PCII relates to threats,
        vulnerabilities, or operational experience related to the
        national infrastructure. PCII offers protection to private
        sector infrastructure information voluntarily shared with
        government entities for purposes of homeland security.
    :cvar LPROT: Protective Order. Stipulation that certain information
        that would normally fall under discovery rules will not be
        disclosed for specifically stated reason.
    :cvar SGI: Safeguards Information. Pursuant to 42 USC 2011, et seq.,
        and as defined in 10 CFR 73.2, SGI relates to security related
        information concerning the physical protection of source,
        byproduct or special nuclear material and the detailed security
        measures for facilities and information contained within
        security plans.
    :cvar SSI: Sensitive Security Information. As defined in 49 C.F.R.
        Part 15.5, Sensitive Security Information is information
        obtained or developed in the conduct of security activities,
        including research and development, the disclosure of which DOT
        has determined would constitute an unwarranted invasion of
        privacy, reveal trade secrets or privileged or confidential
        information, or be detrimental to transportation safety. As
        defined in 49 C.F.R. Part 1520.5, Sensitive Security Information
        is information obtained or developed in the conduct of security
        activities, including research and development, the disclosure
        of which DHS/TSA has determined would, among other things, be
        detrimental to the security of transportation.
    :cvar SSEL: Source Selection. Per FAR 2.101: any of the following
        information that is prepared for use by an agency for the
        purpose of evaluating a bid or proposal to enter into an agency
        procurement contract, if that information has not been
        previously made available to the public or disclosed publicly:
        (Items 1-10).
    :cvar STAT: Statistical Information. Refers to information collected
        by a Federal statistical agency, unit, or program for
        statistical purposes or used for statistical activities; under
        law, regulation, or Government-wide policy such 'Statistical'
        CUI requires: (1) protection from unauthorized disclosure; (2)
        special handling safeguards; and/or (3) prescribed limits on
        access or dissemination.
    :cvar STUD: Student Records. As per 20 USC 1232g, the Family
        Educational Rights and Privacy Act of 1974, an education record
        which is comprised of those records which are directly related
        to a student.
    :cvar TSCA: Toxic Substances. Health, safety, and exposure
        information related to chemical substances, chemical mixtures,
        and articles as defined under the Toxic Substances Control Act
        (TSCA).
    :cvar DCNI: Unclassified Controlled Nuclear Information - Defense.
        Relating to Department of Defense special nuclear material
        (SNM), equipment, and facilities, as defined by 32 CFR 223.
    :cvar UCNI: Unclassified Controlled Nuclear Information - Energy.
        Relating to certain design and security information concerning
        nuclear facilities, materials, and weapons, specific to the
        Department of Energy.
    :cvar CENS: US Census. Related to information gathered by the Bureau
        of the Census during the process of collecting, compiling,
        evaluating, analyzing of demographic, economic, and social data
        pertaining at a specified time to any or all persons in the
        United States and dissemination is limited to those with special
        sworn status, who may only use the data for statistical purposes
        and only for those statistical purposes for which the data was
        supplied.
    :cvar WHSTL: Whistleblower Identity. Identity of anyone providing
        information relating to a legal violation or illicit or unsafe
        activity, including information provided by a whistleblower
        which could reasonably be expected to reveal the identity of a
        whistleblower.
    :cvar WIT: Witness Protection. Information related to the secretive
        details associated with one who has testified or may testify
        under circumstances that require secrecy of that individual and
        details pertaining to that person.
    :cvar WDT: Written Determinations. Rulings, determination letters,
        technical advice memoranda or Chief Counsel Advice, as those
        terms are defined in Treasury Regulation 301.6110-2, which are
        made available for public inspection subject to the withholding
        of certain types of data as enumerated in Treasury Regulation
        301-6110.
    """

    AIV = "AIV"
    ADPO = "ADPO"
    CRITAN = "CRITAN"
    ARCHR = "ARCHR"
    FSEC = "FSEC"
    BUDG = "BUDG"
    FUND = "FUND"
    CVI = "CVI"
    CHLD = "CHLD"
    CCI = "CCI"
    CONTRACT = "CONTRACT"
    SUB = "SUB"
    CTI = "CTI"
    CHRI = "CHRI"
    CEII = "CEII"
    LDNA = "LDNA"
    EXPT = "EXPT"
    JURY = "JURY"
    TAX = "TAX"
    FISA = "FISA"
    FISAB = "FISAB"
    FNC = "FNC"
    INTEL = "INTEL"
    NUC = "NUC"
    PRVCY = "PRVCY"
    PROCURE = "PROCURE"
    PROPIN = "PROPIN"
    GENETIC = "GENETIC"
    GEO = "GEO"
    HLTH = "HLTH"
    HISTP = "HISTP"
    INF = "INF"
    PRIIG = "PRIIG"
    IFNC = "IFNC"
    ID = "ID"
    INTL = "INTL"
    INV = "INV"
    LFNC = "LFNC"
    NPSR = "NPSR"
    NNPI = "NNPI"
    SRI = "SRI"
    PERS = "PERS"
    MFC = "MFC"
    PCII = "PCII"
    LPROT = "LPROT"
    SGI = "SGI"
    SSI = "SSI"
    SSEL = "SSEL"
    STAT = "STAT"
    STUD = "STUD"
    TSCA = "TSCA"
    DCNI = "DCNI"
    UCNI = "UCNI"
    CENS = "CENS"
    WHSTL = "WHSTL"
    WIT = "WIT"
    WDT = "WDT"


class ClassificationEnum(Enum):
    """
    (U) All currently valid classification marks PERMISSIBLE VALUES The
    permissible values for this simple type are defined in the Controlled
    Value Enumeration: CVEnumISMClassificationAll.xml.

    :cvar R: RESTRICTED
    :cvar C: CONFIDENTIAL
    :cvar S: SECRET
    :cvar TS: TOP SECRET
    :cvar U: UNCLASSIFIED
    """

    R = "R"
    C = "C"
    S = "S"
    TS = "TS"
    U = "U"


class DeclassExceptionEnum(Enum):
    """
    (U) All currently authorized authority block declass date/event
    exemptions.

    PERMISSIBLE VALUES The permissible values for this simple type are
    defined in the Controlled Value Enumeration: CVEnumISM25X.xml.

    :cvar AEA: When using a source document that contains portions of
        Restricted Data (RD) or Formerly Restricted Data (FRD) where the
        RD/FRD source document(s) do not have declassification
        instructions, the derivatively classified document shall not
        contain a declassification date or event on the Declassify On
        line. The following shall be annotated on the Declassify On
        line: "Not Applicable or (N/A) to RD/FRD portions" and "See
        source list for NSI portions" separated by a period. The source
        list must include the declassification instruction for each of
        the source documents classified under E.O. 13526 and shall not
        appear in the classification authority block
    :cvar NATO: Since NATO information is not to be declassified or
        downgraded without the prior consent of NATO, the "Declassify
        on" line of documents that commingle information classified by
        NATO and U.S. classified NSI, will read "N/A to NATO portions.
        See source list for NSI portions." The NSI source list will
        appear beneath the classification authority block in a manner
        that clearly identifies it as separate and distinct.
    :cvar NATO_AEA: Handles special case of BOTH NATO and AEA as a
        single exemption.
    :cvar VALUE_25_X1: Reveal the identity of a confidential human
        source, a human intelligence source, a relationship with an
        intelligence or security service of a foreign government or
        international organization, or a non-human intelligence source;
        or impair the effectiveness of an intelligence method currently
        in use, available for use, or under development.
    :cvar VALUE_25_X1_EO_12951: "25X1, EO 12951" (prescribed by the DNI
        for use on information described in E.O. 12951, Release of
        Imagery Acquired by Space-Based National Intelligence
        Reconnaissance Systems)
    :cvar VALUE_25_X2: Reveal information that would assist in the
        development, production, or use of weapons of mass destruction.
    :cvar VALUE_25_X3: Reveal information that would impair U.S.
        cryptologic systems or activities.
    :cvar VALUE_25_X4: Reveal information that would impair the
        application of state-of-the-art technology within a U.S. weapon
        system.
    :cvar VALUE_25_X5: Reveal formally named or numbered U.S. military
        war plans that remain in effect, or reveal operational or
        tactical elements of prior plans that are contained in such
        active plans.
    :cvar VALUE_25_X6: Reveal information, including foreign government
        information, that would cause serious harm to relations between
        the United States and a foreign government, or to ongoing
        diplomatic activities of the United States.
    :cvar VALUE_25_X7: Reveal information that would impair the current
        ability of United States Government officials to protect the
        President, Vice President, and other protectees for whom
        protection services, in the interest of the national security,
        are authorized.
    :cvar VALUE_25_X8: Reveal information that would seriously impair
        current national security emergency preparedness plans or reveal
        current vulnerabilities of systems, installations, or
        infrastructures relating to the national security.
    :cvar VALUE_25_X9: Violate a statute, treaty, or international
        agreement that does not permit the automatic or unilateral
        declassification of information at 25 years.
    :cvar VALUE_50_X1: The ISCAP has authorized use of this code in the
        FBI's classification guidance (which results in a 75-year
        classification period) for any agency sourcing/reusing the
        information.
    :cvar VALUE_50_X1_HUM: When the information clearly and demonstrably
        could be expected to reveal the identity of a confidential human
        source or a human intelligence source.
    :cvar VALUE_50_X2: Reveal information that would assist in the
        development, production, or use of weapons of mass destruction.
    :cvar VALUE_50_X2_WMD: When the information clearly and demonstrably
        could reveal key design concepts of weapons of mass destruction.
    :cvar VALUE_50_X3: Reveal information that would impair U.S.
        cryptologic systems or activities.
    :cvar VALUE_50_X4: Reveal information that would impair the
        application of state-of-the-art technology within a U.S. weapon
        system.
    :cvar VALUE_50_X5: Reveal formally named or numbered U.S. military
        war plans that remain in effect, or reveal operational or
        tactical elements of prior plans that are contained in such
        active plans.
    :cvar VALUE_50_X6: Reveal information, including foreign government
        information, that would cause serious harm to relations between
        the United States and a foreign government, or to ongoing
        diplomatic activities of the United States.
    :cvar VALUE_50_X7: Reveal information that would impair the current
        ability of United States Government officials to protect the
        President, Vice President, and other protectees for whom
        protection services, in the interest of the national security,
        are authorized.
    :cvar VALUE_50_X8: Reveal information that would seriously impair
        current national security emergency preparedness plans or reveal
        current vulnerabilities of systems, installations, or
        infrastructures relating to the national security.
    :cvar VALUE_50_X9: Violate a statute, treaty, or international
        agreement that does not permit the automatic or unilateral
        declassification of information at 25 years.
    :cvar VALUE_75_X: Specific information that has been formally
        approved by the ISCAP as information that does not permit the
        automatic or unilateral declassification of information at 75
        years.
    """

    AEA = "AEA"
    NATO = "NATO"
    NATO_AEA = "NATO_AEA"
    VALUE_25_X1 = "25X1"
    VALUE_25_X1_EO_12951 = "25X1_EO_12951"
    VALUE_25_X2 = "25X2"
    VALUE_25_X3 = "25X3"
    VALUE_25_X4 = "25X4"
    VALUE_25_X5 = "25X5"
    VALUE_25_X6 = "25X6"
    VALUE_25_X7 = "25X7"
    VALUE_25_X8 = "25X8"
    VALUE_25_X9 = "25X9"
    VALUE_50_X1 = "50X1"
    VALUE_50_X1_HUM = "50X1_HUM"
    VALUE_50_X2 = "50X2"
    VALUE_50_X2_WMD = "50X2_WMD"
    VALUE_50_X3 = "50X3"
    VALUE_50_X4 = "50X4"
    VALUE_50_X5 = "50X5"
    VALUE_50_X6 = "50X6"
    VALUE_50_X7 = "50X7"
    VALUE_50_X8 = "50X8"
    VALUE_50_X9 = "50X9"
    VALUE_75_X = "75X"


class DisseminationControlsEnum(Enum):
    """
    (U) All currently valid Dissemination controls from the published
    register PERMISSIBLE VALUES The permissible values for this simple type
    are defined in the Controlled Value Enumeration: CVEnumISMDissem.xml.

    :cvar RS: RISK SENSITIVE
    :cvar FOUO: FOR OFFICIAL USE ONLY
    :cvar OC: ORIGINATOR CONTROLLED
    :cvar OC_USGOV: ORIGINATOR CONTROLLED US GOVERNMENT
    :cvar IMC: CONTROLLED IMAGERY
    :cvar NF: NOT RELEASABLE TO FOREIGN NATIONALS
    :cvar PR: CAUTION-PROPRIETARY INFORMATION INVOLVED
    :cvar REL: AUTHORIZED FOR RELEASE TO
    :cvar RELIDO: RELEASABLE BY INFORMATION DISCLOSURE OFFICIAL
    :cvar EYES: EYES ONLY
    :cvar DSEN: DEA SENSITIVE
    :cvar RAWFISA: RAW FOREIGN INTELLIGENCE SURVEILLANCE ACT
    :cvar FISA: FOREIGN INTELLIGENCE SURVEILLANCE ACT
    :cvar DISPLAYONLY: AUTHORIZED FOR DISPLAY BUT NOT RELEASE TO
    :cvar EXEMPT_FROM_ICD501_DISCOVERY: EXEMPT FROM ICD501 DISCOVERY
    :cvar WAIVED: WAIVED
    :cvar AC: Attorney-Client
    :cvar AWP: Attorney-WP
    :cvar DL_ONLY: DL ONLY
    :cvar FED_ONLY: FED ONLY
    :cvar FEDCON: FEDCON
    :cvar NOCON: NOCON
    """

    RS = "RS"
    FOUO = "FOUO"
    OC = "OC"
    OC_USGOV = "OC_USGOV"
    IMC = "IMC"
    NF = "NF"
    PR = "PR"
    REL = "REL"
    RELIDO = "RELIDO"
    EYES = "EYES"
    DSEN = "DSEN"
    RAWFISA = "RAWFISA"
    FISA = "FISA"
    DISPLAYONLY = "DISPLAYONLY"
    EXEMPT_FROM_ICD501_DISCOVERY = "EXEMPT_FROM_ICD501_DISCOVERY"
    WAIVED = "WAIVED"
    AC = "AC"
    AWP = "AWP"
    DL_ONLY = "DL_ONLY"
    FED_ONLY = "FED_ONLY"
    FEDCON = "FEDCON"
    NOCON = "NOCON"


class FgiSourceOpenEnum(Enum):
    """
    CVEnumISMCATFGIOpen Values.

    :cvar ABW: Aruba
    :cvar AFG: Islamic Republic of Afghanistan
    :cvar AGO: Republic of Angola
    :cvar AIA: Anguilla
    :cvar ALB: Republic of Albania
    :cvar AND: Principality of Andorra
    :cvar ARE: United Arab Emirates
    :cvar ARG: Argentine Republic
    :cvar ARM: Republic of Armenia
    :cvar ASM: Territory of American Samoa
    :cvar ATA: Antarctica
    :cvar ATF: French Southern and Antarctic Lands
    :cvar ATG: Antigua and Barbuda
    :cvar AUS: Commonwealth of Australia
    :cvar AUT: Republic of Austria
    :cvar AX1: Unknown
    :cvar AX2: Guantanamo Bay Naval Base
    :cvar AX3: Entity 6
    :cvar AZE: Republic of Azerbaijan
    :cvar BDI: Republic of Burundi
    :cvar BEL: Kingdom of Belgium
    :cvar BEN: Republic of Benin
    :cvar BES: Bonaire, Sint Eustatius, and Saba
    :cvar BFA: Burkina Faso
    :cvar BGD: People's Republic of Bangladesh
    :cvar BGR: Republic of Bulgaria
    :cvar BHR: Kingdom of Bahrain
    :cvar BHS: Commonwealth of The Bahamas
    :cvar BIH: Bosnia and Herzegovina
    :cvar BLM: Saint Barthelemy
    :cvar BLR: Republic of Belarus
    :cvar BLZ: Belize
    :cvar BMU: Bermuda
    :cvar BOL: Plurinational State of Bolivia
    :cvar BRA: Federative Republic of Brazil
    :cvar BRB: Barbados
    :cvar BRN: Brunei Darussalam
    :cvar BTN: Kingdom of Bhutan
    :cvar BVT: Bouvet Island
    :cvar BWA: Republic of Botswana
    :cvar CAF: Central African Republic
    :cvar CAN: Canada
    :cvar CCK: Territory of Cocos (Keeling) Islands
    :cvar CHE: Swiss Confederation
    :cvar CHL: Republic of Chile
    :cvar CHN: People's Republic of China
    :cvar CIV: Republic of Côte d'Ivoire
    :cvar CMR: Republic of Cameroon
    :cvar COD: Democratic Republic of the Congo
    :cvar COG: Republic of the Congo
    :cvar COK: Cook Islands
    :cvar COL: Republic of Colombia
    :cvar COM: Union of the Comoros
    :cvar CPT: Clipperton Island
    :cvar CPV: Republic of Cabo Verde
    :cvar CRI: Republic of Costa Rica
    :cvar CUB: Republic of Cuba
    :cvar CUW: Curaçao
    :cvar CXR: Territory of Christmas Island
    :cvar CYM: Cayman Islands
    :cvar CYP: Republic of Cyprus
    :cvar CZE: Czech Republic
    :cvar DEU: Federal Republic of Germany
    :cvar DGA: Diego Garcia
    :cvar DJI: Republic of Djibouti
    :cvar DMA: Commonwealth of Dominica
    :cvar DNK: Kingdom of Denmark
    :cvar DOM: Dominican Republic
    :cvar DZA: People's Democratic Republic of Algeria
    :cvar ECU: Republic of Ecuador
    :cvar EGY: Arab Republic of Egypt
    :cvar ERI: State of Eritrea
    :cvar ESH: Western Sahara
    :cvar ESP: Kingdom of Spain
    :cvar EST: Republic of Estonia
    :cvar ETH: Federal Democratic Republic of Ethiopia
    :cvar FIN: Republic of Finland
    :cvar FJI: Republic of Fiji
    :cvar FLK: Falkland Islands (Islas Malvinas)
    :cvar FRA: French Republic
    :cvar FRO: Faroe Islands
    :cvar FSM: Federated States of Micronesia
    :cvar GAB: Gabonese Republic
    :cvar GBR: United Kingdom of Great Britain and Northern Ireland
    :cvar GEO: Georgia
    :cvar GGY: Bailiwick of Guernsey
    :cvar GHA: Republic of Ghana
    :cvar GIB: Gibraltar
    :cvar GIN: Republic of Guinea
    :cvar GLP: Region of Guadeloupe
    :cvar GMB: Republic of The Gambia
    :cvar GNB: Republic of Guinea-Bissau
    :cvar GNQ: Republic of Equatorial Guinea
    :cvar GRC: Hellenic Republic
    :cvar GRD: Grenada
    :cvar GRL: Greenland
    :cvar GTM: Republic of Guatemala
    :cvar GUF: Territorial Collectivity of Guiana
    :cvar GUM: Territory of Guam
    :cvar GUY: Co-operative Republic of Guyana
    :cvar HKG: Hong Kong Special Administrative Region
    :cvar HMD: Territory of Heard Island and McDonald Islands
    :cvar HND: Republic of Honduras
    :cvar HRV: Republic of Croatia
    :cvar HTI: Republic of Haiti
    :cvar HUN: Hungary
    :cvar IDN: Republic of Indonesia
    :cvar IMN: Isle of Man
    :cvar IND: Republic of India
    :cvar IOT: British Indian Ocean Territory
    :cvar IRL: Ireland
    :cvar IRN: Islamic Republic of Iran
    :cvar IRQ: Republic of Iraq
    :cvar ISL: Republic of Iceland
    :cvar ISR: State of Israel
    :cvar ITA: Italian Republic
    :cvar JAM: Jamaica
    :cvar JEY: Bailiwick of Jersey
    :cvar JOR: Hashemite Kingdom of Jordan
    :cvar JPN: Japan
    :cvar KAZ: Republic of Kazakhstan
    :cvar KEN: Republic of Kenya
    :cvar KGZ: Kyrgyz Republic
    :cvar KHM: Kingdom of Cambodia
    :cvar KIR: Republic of Kiribati
    :cvar KNA: Federation of Saint Kitts and Nevis
    :cvar KOR: Republic of Korea
    :cvar KWT: State of Kuwait
    :cvar LAO: Lao People's Democratic Republic
    :cvar LBN: Lebanese Republic
    :cvar LBR: Republic of Liberia
    :cvar LBY: State of Libya
    :cvar LCA: Saint Lucia
    :cvar LIE: Principality of Liechtenstein
    :cvar LKA: Democratic Socialist Republic of Sri Lanka
    :cvar LSO: Kingdom of Lesotho
    :cvar LTU: Republic of Lithuania
    :cvar LUX: Grand Duchy of Luxembourg
    :cvar LVA: Republic of Latvia
    :cvar MAC: Macau Special Administrative Region
    :cvar MAF: Saint Martin
    :cvar MAR: Kingdom of Morocco
    :cvar MCO: Principality of Monaco
    :cvar MDA: Republic of Moldova
    :cvar MDG: Republic of Madagascar
    :cvar MDV: Republic of Maldives
    :cvar MEX: United Mexican States
    :cvar MHL: Republic of the Marshall Islands
    :cvar MKD: Republic of North Macedonia
    :cvar MLI: Republic of Mali
    :cvar MLT: Republic of Malta
    :cvar MMR: Union of Burma
    :cvar MNE: Montenegro
    :cvar MNG: Mongolia
    :cvar MNP: Commonwealth of the Northern Mariana Islands
    :cvar MOZ: Republic of Mozambique
    :cvar MRT: Islamic Republic of Mauritania
    :cvar MSR: Montserrat
    :cvar MTQ: Territorial Collectivity of Martinique
    :cvar MUS: Republic of Mauritius
    :cvar MWI: Republic of Malawi
    :cvar MYS: Malaysia
    :cvar MYT: Department of Mayotte
    :cvar NAM: Republic of Namibia
    :cvar NCL: New Caledonia
    :cvar NER: Republic of Niger
    :cvar NFK: Territory of Norfolk Island
    :cvar NGA: Federal Republic of Nigeria
    :cvar NIC: Republic of Nicaragua
    :cvar NIU: Niue
    :cvar NLD: Kingdom of the Netherlands
    :cvar NOR: Kingdom of Norway
    :cvar NPL: Federal Democratic Republic of Nepal
    :cvar NRU: Republic of Nauru
    :cvar NZL: New Zealand
    :cvar OMN: Sultanate of Oman
    :cvar PAK: Islamic Republic of Pakistan
    :cvar PAN: Republic of Panama
    :cvar PCN: Pitcairn, Henderson, Ducie, and Oeno Islands
    :cvar PER: Republic of Peru
    :cvar PHL: Republic of the Philippines
    :cvar PLW: Republic of Palau
    :cvar PNG: Independent State of Papua New Guinea
    :cvar POL: Republic of Poland
    :cvar PRI: Commonwealth of Puerto Rico
    :cvar PRK: Democratic People's Republic of Korea
    :cvar PRT: Portuguese Republic
    :cvar PRY: Republic of Paraguay
    :cvar PYF: French Polynesia
    :cvar QAT: State of Qatar
    :cvar REU: Region of Reunion
    :cvar ROU: Romania
    :cvar RUS: Russian Federation
    :cvar RWA: Republic of Rwanda
    :cvar SAU: Kingdom of Saudi Arabia
    :cvar SDN: Republic of the Sudan
    :cvar SEN: Republic of Senegal
    :cvar SGP: Republic of Singapore
    :cvar SGS: South Georgia and the South Sandwich Islands
    :cvar SHN: Saint Helena, Ascension, and Tristan da Cunha
    :cvar SLB: Solomon Islands
    :cvar SLE: Republic of Sierra Leone
    :cvar SLV: Republic of El Salvador
    :cvar SMR: Republic of San Marino
    :cvar SOM: Federal Republic of Somalia
    :cvar SPM: Territorial Collectivity of Saint Pierre and Miquelon
    :cvar SRB: Republic of Serbia
    :cvar SSD: Republic of South Sudan
    :cvar STP: Democratic Republic of Sao Tome and Principe
    :cvar SUR: Republic of Suriname
    :cvar SVK: Slovak Republic
    :cvar SVN: Republic of Slovenia
    :cvar SWE: Kingdom of Sweden
    :cvar SWZ: Kingdom of Eswatini
    :cvar SXM: Sint Maarten
    :cvar SYC: Republic of Seychelles
    :cvar SYR: Syrian Arab Republic
    :cvar TCA: Turks and Caicos Islands
    :cvar TCD: Republic of Chad
    :cvar TGO: Togolese Republic
    :cvar THA: Kingdom of Thailand
    :cvar TJK: Republic of Tajikistan
    :cvar TKL: Tokelau
    :cvar TKM: Turkmenistan
    :cvar TLS: Democratic Republic of Timor-Leste
    :cvar TON: Kingdom of Tonga
    :cvar TTO: Republic of Trinidad and Tobago
    :cvar TUN: Republic of Tunisia
    :cvar TUR: Republic of Turkey
    :cvar TUV: Tuvalu
    :cvar TWN: Taiwan
    :cvar TZA: United Republic of Tanzania
    :cvar UGA: Republic of Uganda
    :cvar UKR: Ukraine
    :cvar URY: Oriental Republic of Uruguay
    :cvar UZB: Republic of Uzbekistan
    :cvar VAT: State of the Vatican City
    :cvar VCT: Saint Vincent and the Grenadines
    :cvar VEN: Bolivarian Republic of Venezuela
    :cvar VGB: British Virgin Islands
    :cvar VIR: United States Virgin Islands
    :cvar VNM: Socialist Republic of Vietnam
    :cvar VUT: Republic of Vanuatu
    :cvar WLF: Wallis and Futuna
    :cvar WSM: Independent State of Samoa
    :cvar XAC: Territory of Ashmore and Cartier Islands
    :cvar XAZ: Entity 1
    :cvar XBI: Bassas da India
    :cvar XBK: Baker Island
    :cvar XCR: Entity 2
    :cvar XCS: Coral Sea Islands Territory
    :cvar XCY: Entity 3
    :cvar XEU: Europa Island
    :cvar XGL: Glorioso Islands
    :cvar XGZ: Gaza Strip
    :cvar XHO: Howland Island
    :cvar XJA: Johnston Atoll
    :cvar XJM: Jan Mayen
    :cvar XJN: Juan de Nova Island
    :cvar XJV: Jarvis Island
    :cvar XKM: Entity 4
    :cvar XKN: Entity 5
    :cvar XKR: Kingman Reef
    :cvar XKS: Republic of Kosovo
    :cvar XMW: Midway Islands
    :cvar XNV: Navassa Island
    :cvar XPL: Palmyra Atoll
    :cvar XPR: Paracel Islands
    :cvar XQZ: Akrotiri
    :cvar XSP: Spratly Islands
    :cvar XSV: Svalbard
    :cvar XTR: Tromelin Island
    :cvar XWB: West Bank
    :cvar XWK: Wake Island
    :cvar XXD: Dhekelia
    :cvar YEM: Republic of Yemen
    :cvar ZAF: Republic of South Africa
    :cvar ZMB: Republic of Zambia
    :cvar ZWE: Republic of Zimbabwe
    :cvar ACGU: FOUR EYES
    :cvar AMSP: AFRICOM Multinational Strategic Partners
    :cvar AOSC: Athens Olympics Security Coalition
    :cvar APFS: African Peacekeeping Force Somalia
    :cvar ASEA: Association of Southeast Asian Nations (ASEAN)
    :cvar AUSTRALIA_GROUP: Australia Group
    :cvar BHTF: Boko Haram Task Force
    :cvar BWCS: Biological Weapons Convention States
    :cvar CFCK: Combined Forces Command Korea
    :cvar CFOD: Coalition Forces Odyssey Dawn
    :cvar CFUP: Coalition Forces Unified Protector
    :cvar CLFC: Combined Libya Fusion Cell
    :cvar CMFC: Combined Maritime Forces Central
    :cvar CMFP: Cooperative Maritime Forces Pacific
    :cvar CPMT: Civilian Protection Monitoring Team for Sudan
    :cvar CTOC: Countering Transnational Organized Crime
    :cvar CWCS: Chemical Weapons Convention States
    :cvar ECTF: European Counter-Terrorism Forces
    :cvar EFOR: European Union Stabilization Forces in Bosnia
    :cvar EU: European Union
    :cvar EUDA: European Union DARFUR
    :cvar FRME: Counter Violent Extremist Organizations Framework
        Partners
    :cvar FVEY: FIVE EYES
    :cvar GCCH: Gulf Cooperation Council
    :cvar GCTF: Global Counter-Terrorism Forces
    :cvar GFNX: Global Foreign Terrorist Fighter Network Exchange
    :cvar GMIF: Global Maritime Interception Forces
    :cvar IESC: International Events Security Coalition
    :cvar IMSC: International Maritime Security Construct
    :cvar IMSP: INDOPACOM Multinational Strategic Partners
    :cvar IPMC: INDO PACIFIC Maritime Call
    :cvar IRKS: Inherent Resolve Kinetic Support
    :cvar ISAF: International Security Assistance Force for Afghanistan
    :cvar ISSG: International Syria Support Group
    :cvar KFOR: Stabilization Forces in Kosovo
    :cvar MCFI: Multinational Coalition Forces-Iraq
    :cvar MESF: Middle East Stability Force
    :cvar MGEU: Multinational GEOINT Europe
    :cvar MIFH: Multinational Interim Force Haiti
    :cvar MLEC: Multi-Lateral Enduring Contingency
    :cvar MNTF: Multinational Task Force
    :cvar MPFL: Multinational Peacekeeping Forces
    :cvar NACT: North African Counter-Terrorism Forces
    :cvar NATO: North Atlantic Treaty Organization
    :cvar NCFE: NATO CFE Treaty on Conventional Armed Forces in Europe
    :cvar NKIC: North Korea Intelligence Coalition
    :cvar NRDC: NORDIC
    :cvar NSG: Nuclear Suppliers' Group
    :cvar OSAG: Olympic Security Advisory Group
    :cvar OSTY: Open Skies Treaty
    :cvar PAWA: Partnership for Actions in West Africa
    :cvar PGMF: Persian Gulf Multinational Forces
    :cvar PSMX: Pacific Security Monitoring Exchange
    :cvar RISC: Russia Intelligence Sharing Coalition
    :cvar RSMA: Resolute Support Mission Afghanistan
    :cvar SFOR: Stabilization Force
    :cvar SOFP: Special Operations Forces Partners
    :cvar SPAA: SOF Planning Activities in Afghanistan (also called
        "11-Eyes")
    :cvar TEYE: THREE EYES
    :cvar TFTC: Terrorist Financing Targeting Center
    :cvar UNCK: United Nations Command, Korea
    """

    ABW = "ABW"
    AFG = "AFG"
    AGO = "AGO"
    AIA = "AIA"
    ALB = "ALB"
    AND = "AND"
    ARE = "ARE"
    ARG = "ARG"
    ARM = "ARM"
    ASM = "ASM"
    ATA = "ATA"
    ATF = "ATF"
    ATG = "ATG"
    AUS = "AUS"
    AUT = "AUT"
    AX1 = "AX1"
    AX2 = "AX2"
    AX3 = "AX3"
    AZE = "AZE"
    BDI = "BDI"
    BEL = "BEL"
    BEN = "BEN"
    BES = "BES"
    BFA = "BFA"
    BGD = "BGD"
    BGR = "BGR"
    BHR = "BHR"
    BHS = "BHS"
    BIH = "BIH"
    BLM = "BLM"
    BLR = "BLR"
    BLZ = "BLZ"
    BMU = "BMU"
    BOL = "BOL"
    BRA = "BRA"
    BRB = "BRB"
    BRN = "BRN"
    BTN = "BTN"
    BVT = "BVT"
    BWA = "BWA"
    CAF = "CAF"
    CAN = "CAN"
    CCK = "CCK"
    CHE = "CHE"
    CHL = "CHL"
    CHN = "CHN"
    CIV = "CIV"
    CMR = "CMR"
    COD = "COD"
    COG = "COG"
    COK = "COK"
    COL = "COL"
    COM = "COM"
    CPT = "CPT"
    CPV = "CPV"
    CRI = "CRI"
    CUB = "CUB"
    CUW = "CUW"
    CXR = "CXR"
    CYM = "CYM"
    CYP = "CYP"
    CZE = "CZE"
    DEU = "DEU"
    DGA = "DGA"
    DJI = "DJI"
    DMA = "DMA"
    DNK = "DNK"
    DOM = "DOM"
    DZA = "DZA"
    ECU = "ECU"
    EGY = "EGY"
    ERI = "ERI"
    ESH = "ESH"
    ESP = "ESP"
    EST = "EST"
    ETH = "ETH"
    FIN = "FIN"
    FJI = "FJI"
    FLK = "FLK"
    FRA = "FRA"
    FRO = "FRO"
    FSM = "FSM"
    GAB = "GAB"
    GBR = "GBR"
    GEO = "GEO"
    GGY = "GGY"
    GHA = "GHA"
    GIB = "GIB"
    GIN = "GIN"
    GLP = "GLP"
    GMB = "GMB"
    GNB = "GNB"
    GNQ = "GNQ"
    GRC = "GRC"
    GRD = "GRD"
    GRL = "GRL"
    GTM = "GTM"
    GUF = "GUF"
    GUM = "GUM"
    GUY = "GUY"
    HKG = "HKG"
    HMD = "HMD"
    HND = "HND"
    HRV = "HRV"
    HTI = "HTI"
    HUN = "HUN"
    IDN = "IDN"
    IMN = "IMN"
    IND = "IND"
    IOT = "IOT"
    IRL = "IRL"
    IRN = "IRN"
    IRQ = "IRQ"
    ISL = "ISL"
    ISR = "ISR"
    ITA = "ITA"
    JAM = "JAM"
    JEY = "JEY"
    JOR = "JOR"
    JPN = "JPN"
    KAZ = "KAZ"
    KEN = "KEN"
    KGZ = "KGZ"
    KHM = "KHM"
    KIR = "KIR"
    KNA = "KNA"
    KOR = "KOR"
    KWT = "KWT"
    LAO = "LAO"
    LBN = "LBN"
    LBR = "LBR"
    LBY = "LBY"
    LCA = "LCA"
    LIE = "LIE"
    LKA = "LKA"
    LSO = "LSO"
    LTU = "LTU"
    LUX = "LUX"
    LVA = "LVA"
    MAC = "MAC"
    MAF = "MAF"
    MAR = "MAR"
    MCO = "MCO"
    MDA = "MDA"
    MDG = "MDG"
    MDV = "MDV"
    MEX = "MEX"
    MHL = "MHL"
    MKD = "MKD"
    MLI = "MLI"
    MLT = "MLT"
    MMR = "MMR"
    MNE = "MNE"
    MNG = "MNG"
    MNP = "MNP"
    MOZ = "MOZ"
    MRT = "MRT"
    MSR = "MSR"
    MTQ = "MTQ"
    MUS = "MUS"
    MWI = "MWI"
    MYS = "MYS"
    MYT = "MYT"
    NAM = "NAM"
    NCL = "NCL"
    NER = "NER"
    NFK = "NFK"
    NGA = "NGA"
    NIC = "NIC"
    NIU = "NIU"
    NLD = "NLD"
    NOR = "NOR"
    NPL = "NPL"
    NRU = "NRU"
    NZL = "NZL"
    OMN = "OMN"
    PAK = "PAK"
    PAN = "PAN"
    PCN = "PCN"
    PER = "PER"
    PHL = "PHL"
    PLW = "PLW"
    PNG = "PNG"
    POL = "POL"
    PRI = "PRI"
    PRK = "PRK"
    PRT = "PRT"
    PRY = "PRY"
    PYF = "PYF"
    QAT = "QAT"
    REU = "REU"
    ROU = "ROU"
    RUS = "RUS"
    RWA = "RWA"
    SAU = "SAU"
    SDN = "SDN"
    SEN = "SEN"
    SGP = "SGP"
    SGS = "SGS"
    SHN = "SHN"
    SLB = "SLB"
    SLE = "SLE"
    SLV = "SLV"
    SMR = "SMR"
    SOM = "SOM"
    SPM = "SPM"
    SRB = "SRB"
    SSD = "SSD"
    STP = "STP"
    SUR = "SUR"
    SVK = "SVK"
    SVN = "SVN"
    SWE = "SWE"
    SWZ = "SWZ"
    SXM = "SXM"
    SYC = "SYC"
    SYR = "SYR"
    TCA = "TCA"
    TCD = "TCD"
    TGO = "TGO"
    THA = "THA"
    TJK = "TJK"
    TKL = "TKL"
    TKM = "TKM"
    TLS = "TLS"
    TON = "TON"
    TTO = "TTO"
    TUN = "TUN"
    TUR = "TUR"
    TUV = "TUV"
    TWN = "TWN"
    TZA = "TZA"
    UGA = "UGA"
    UKR = "UKR"
    URY = "URY"
    UZB = "UZB"
    VAT = "VAT"
    VCT = "VCT"
    VEN = "VEN"
    VGB = "VGB"
    VIR = "VIR"
    VNM = "VNM"
    VUT = "VUT"
    WLF = "WLF"
    WSM = "WSM"
    XAC = "XAC"
    XAZ = "XAZ"
    XBI = "XBI"
    XBK = "XBK"
    XCR = "XCR"
    XCS = "XCS"
    XCY = "XCY"
    XEU = "XEU"
    XGL = "XGL"
    XGZ = "XGZ"
    XHO = "XHO"
    XJA = "XJA"
    XJM = "XJM"
    XJN = "XJN"
    XJV = "XJV"
    XKM = "XKM"
    XKN = "XKN"
    XKR = "XKR"
    XKS = "XKS"
    XMW = "XMW"
    XNV = "XNV"
    XPL = "XPL"
    XPR = "XPR"
    XQZ = "XQZ"
    XSP = "XSP"
    XSV = "XSV"
    XTR = "XTR"
    XWB = "XWB"
    XWK = "XWK"
    XXD = "XXD"
    YEM = "YEM"
    ZAF = "ZAF"
    ZMB = "ZMB"
    ZWE = "ZWE"
    ACGU = "ACGU"
    AMSP = "AMSP"
    AOSC = "AOSC"
    APFS = "APFS"
    ASEA = "ASEA"
    AUSTRALIA_GROUP = "AUSTRALIA_GROUP"
    BHTF = "BHTF"
    BWCS = "BWCS"
    CFCK = "CFCK"
    CFOD = "CFOD"
    CFUP = "CFUP"
    CLFC = "CLFC"
    CMFC = "CMFC"
    CMFP = "CMFP"
    CPMT = "CPMT"
    CTOC = "CTOC"
    CWCS = "CWCS"
    ECTF = "ECTF"
    EFOR = "EFOR"
    EU = "EU"
    EUDA = "EUDA"
    FRME = "FRME"
    FVEY = "FVEY"
    GCCH = "GCCH"
    GCTF = "GCTF"
    GFNX = "GFNX"
    GMIF = "GMIF"
    IESC = "IESC"
    IMSC = "IMSC"
    IMSP = "IMSP"
    IPMC = "IPMC"
    IRKS = "IRKS"
    ISAF = "ISAF"
    ISSG = "ISSG"
    KFOR = "KFOR"
    MCFI = "MCFI"
    MESF = "MESF"
    MGEU = "MGEU"
    MIFH = "MIFH"
    MLEC = "MLEC"
    MNTF = "MNTF"
    MPFL = "MPFL"
    NACT = "NACT"
    NATO = "NATO"
    NCFE = "NCFE"
    NKIC = "NKIC"
    NRDC = "NRDC"
    NSG = "NSG"
    OSAG = "OSAG"
    OSTY = "OSTY"
    PAWA = "PAWA"
    PGMF = "PGMF"
    PSMX = "PSMX"
    RISC = "RISC"
    RSMA = "RSMA"
    SFOR = "SFOR"
    SOFP = "SOFP"
    SPAA = "SPAA"
    TEYE = "TEYE"
    TFTC = "TFTC"
    UNCK = "UNCK"


class FgiSourceProtectedEnum(Enum):
    """
    CVEnumISMCATFGIProtected Values.

    :cvar FGI: Foreign Government Information
    :cvar ABW: Aruba
    :cvar AFG: Islamic Republic of Afghanistan
    :cvar AGO: Republic of Angola
    :cvar AIA: Anguilla
    :cvar ALB: Republic of Albania
    :cvar AND: Principality of Andorra
    :cvar ARE: United Arab Emirates
    :cvar ARG: Argentine Republic
    :cvar ARM: Republic of Armenia
    :cvar ASM: Territory of American Samoa
    :cvar ATA: Antarctica
    :cvar ATF: French Southern and Antarctic Lands
    :cvar ATG: Antigua and Barbuda
    :cvar AUS: Commonwealth of Australia
    :cvar AUT: Republic of Austria
    :cvar AX2: Guantanamo Bay Naval Base
    :cvar AX3: Entity 6
    :cvar AZE: Republic of Azerbaijan
    :cvar BDI: Republic of Burundi
    :cvar BEL: Kingdom of Belgium
    :cvar BEN: Republic of Benin
    :cvar BES: Bonaire, Sint Eustatius, and Saba
    :cvar BFA: Burkina Faso
    :cvar BGD: People's Republic of Bangladesh
    :cvar BGR: Republic of Bulgaria
    :cvar BHR: Kingdom of Bahrain
    :cvar BHS: Commonwealth of The Bahamas
    :cvar BIH: Bosnia and Herzegovina
    :cvar BLM: Saint Barthelemy
    :cvar BLR: Republic of Belarus
    :cvar BLZ: Belize
    :cvar BMU: Bermuda
    :cvar BOL: Plurinational State of Bolivia
    :cvar BRA: Federative Republic of Brazil
    :cvar BRB: Barbados
    :cvar BRN: Brunei Darussalam
    :cvar BTN: Kingdom of Bhutan
    :cvar BVT: Bouvet Island
    :cvar BWA: Republic of Botswana
    :cvar CAF: Central African Republic
    :cvar CAN: Canada
    :cvar CCK: Territory of Cocos (Keeling) Islands
    :cvar CHE: Swiss Confederation
    :cvar CHL: Republic of Chile
    :cvar CHN: People's Republic of China
    :cvar CIV: Republic of Côte d'Ivoire
    :cvar CMR: Republic of Cameroon
    :cvar COD: Democratic Republic of the Congo
    :cvar COG: Republic of the Congo
    :cvar COK: Cook Islands
    :cvar COL: Republic of Colombia
    :cvar COM: Union of the Comoros
    :cvar CPT: Clipperton Island
    :cvar CPV: Republic of Cabo Verde
    :cvar CRI: Republic of Costa Rica
    :cvar CUB: Republic of Cuba
    :cvar CUW: Curaçao
    :cvar CXR: Territory of Christmas Island
    :cvar CYM: Cayman Islands
    :cvar CYP: Republic of Cyprus
    :cvar CZE: Czech Republic
    :cvar DEU: Federal Republic of Germany
    :cvar DGA: Diego Garcia
    :cvar DJI: Republic of Djibouti
    :cvar DMA: Commonwealth of Dominica
    :cvar DNK: Kingdom of Denmark
    :cvar DOM: Dominican Republic
    :cvar DZA: People's Democratic Republic of Algeria
    :cvar ECU: Republic of Ecuador
    :cvar EGY: Arab Republic of Egypt
    :cvar ERI: State of Eritrea
    :cvar ESH: Western Sahara
    :cvar ESP: Kingdom of Spain
    :cvar EST: Republic of Estonia
    :cvar ETH: Federal Democratic Republic of Ethiopia
    :cvar FIN: Republic of Finland
    :cvar FJI: Republic of Fiji
    :cvar FLK: Falkland Islands (Islas Malvinas)
    :cvar FRA: French Republic
    :cvar FRO: Faroe Islands
    :cvar FSM: Federated States of Micronesia
    :cvar GAB: Gabonese Republic
    :cvar GBR: United Kingdom of Great Britain and Northern Ireland
    :cvar GEO: Georgia
    :cvar GGY: Bailiwick of Guernsey
    :cvar GHA: Republic of Ghana
    :cvar GIB: Gibraltar
    :cvar GIN: Republic of Guinea
    :cvar GLP: Region of Guadeloupe
    :cvar GMB: Republic of The Gambia
    :cvar GNB: Republic of Guinea-Bissau
    :cvar GNQ: Republic of Equatorial Guinea
    :cvar GRC: Hellenic Republic
    :cvar GRD: Grenada
    :cvar GRL: Greenland
    :cvar GTM: Republic of Guatemala
    :cvar GUF: Territorial Collectivity of Guiana
    :cvar GUM: Territory of Guam
    :cvar GUY: Co-operative Republic of Guyana
    :cvar HKG: Hong Kong Special Administrative Region
    :cvar HMD: Territory of Heard Island and McDonald Islands
    :cvar HND: Republic of Honduras
    :cvar HRV: Republic of Croatia
    :cvar HTI: Republic of Haiti
    :cvar HUN: Hungary
    :cvar IDN: Republic of Indonesia
    :cvar IMN: Isle of Man
    :cvar IND: Republic of India
    :cvar IOT: British Indian Ocean Territory
    :cvar IRL: Ireland
    :cvar IRN: Islamic Republic of Iran
    :cvar IRQ: Republic of Iraq
    :cvar ISL: Republic of Iceland
    :cvar ISR: State of Israel
    :cvar ITA: Italian Republic
    :cvar JAM: Jamaica
    :cvar JEY: Bailiwick of Jersey
    :cvar JOR: Hashemite Kingdom of Jordan
    :cvar JPN: Japan
    :cvar KAZ: Republic of Kazakhstan
    :cvar KEN: Republic of Kenya
    :cvar KGZ: Kyrgyz Republic
    :cvar KHM: Kingdom of Cambodia
    :cvar KIR: Republic of Kiribati
    :cvar KNA: Federation of Saint Kitts and Nevis
    :cvar KOR: Republic of Korea
    :cvar KWT: State of Kuwait
    :cvar LAO: Lao People's Democratic Republic
    :cvar LBN: Lebanese Republic
    :cvar LBR: Republic of Liberia
    :cvar LBY: State of Libya
    :cvar LCA: Saint Lucia
    :cvar LIE: Principality of Liechtenstein
    :cvar LKA: Democratic Socialist Republic of Sri Lanka
    :cvar LSO: Kingdom of Lesotho
    :cvar LTU: Republic of Lithuania
    :cvar LUX: Grand Duchy of Luxembourg
    :cvar LVA: Republic of Latvia
    :cvar MAC: Macau Special Administrative Region
    :cvar MAF: Saint Martin
    :cvar MAR: Kingdom of Morocco
    :cvar MCO: Principality of Monaco
    :cvar MDA: Republic of Moldova
    :cvar MDG: Republic of Madagascar
    :cvar MDV: Republic of Maldives
    :cvar MEX: United Mexican States
    :cvar MHL: Republic of the Marshall Islands
    :cvar MKD: Republic of North Macedonia
    :cvar MLI: Republic of Mali
    :cvar MLT: Republic of Malta
    :cvar MMR: Union of Burma
    :cvar MNE: Montenegro
    :cvar MNG: Mongolia
    :cvar MNP: Commonwealth of the Northern Mariana Islands
    :cvar MOZ: Republic of Mozambique
    :cvar MRT: Islamic Republic of Mauritania
    :cvar MSR: Montserrat
    :cvar MTQ: Territorial Collectivity of Martinique
    :cvar MUS: Republic of Mauritius
    :cvar MWI: Republic of Malawi
    :cvar MYS: Malaysia
    :cvar MYT: Department of Mayotte
    :cvar NAM: Republic of Namibia
    :cvar NCL: New Caledonia
    :cvar NER: Republic of Niger
    :cvar NFK: Territory of Norfolk Island
    :cvar NGA: Federal Republic of Nigeria
    :cvar NIC: Republic of Nicaragua
    :cvar NIU: Niue
    :cvar NLD: Kingdom of the Netherlands
    :cvar NOR: Kingdom of Norway
    :cvar NPL: Federal Democratic Republic of Nepal
    :cvar NRU: Republic of Nauru
    :cvar NZL: New Zealand
    :cvar OMN: Sultanate of Oman
    :cvar PAK: Islamic Republic of Pakistan
    :cvar PAN: Republic of Panama
    :cvar PCN: Pitcairn, Henderson, Ducie, and Oeno Islands
    :cvar PER: Republic of Peru
    :cvar PHL: Republic of the Philippines
    :cvar PLW: Republic of Palau
    :cvar PNG: Independent State of Papua New Guinea
    :cvar POL: Republic of Poland
    :cvar PRI: Commonwealth of Puerto Rico
    :cvar PRK: Democratic People's Republic of Korea
    :cvar PRT: Portuguese Republic
    :cvar PRY: Republic of Paraguay
    :cvar PYF: French Polynesia
    :cvar QAT: State of Qatar
    :cvar REU: Region of Reunion
    :cvar ROU: Romania
    :cvar RUS: Russian Federation
    :cvar RWA: Republic of Rwanda
    :cvar SAU: Kingdom of Saudi Arabia
    :cvar SDN: Republic of the Sudan
    :cvar SEN: Republic of Senegal
    :cvar SGP: Republic of Singapore
    :cvar SGS: South Georgia and the South Sandwich Islands
    :cvar SHN: Saint Helena, Ascension, and Tristan da Cunha
    :cvar SLB: Solomon Islands
    :cvar SLE: Republic of Sierra Leone
    :cvar SLV: Republic of El Salvador
    :cvar SMR: Republic of San Marino
    :cvar SOM: Federal Republic of Somalia
    :cvar SPM: Territorial Collectivity of Saint Pierre and Miquelon
    :cvar SRB: Republic of Serbia
    :cvar SSD: Republic of South Sudan
    :cvar STP: Democratic Republic of Sao Tome and Principe
    :cvar SUR: Republic of Suriname
    :cvar SVK: Slovak Republic
    :cvar SVN: Republic of Slovenia
    :cvar SWE: Kingdom of Sweden
    :cvar SWZ: Kingdom of Eswatini
    :cvar SXM: Sint Maarten
    :cvar SYC: Republic of Seychelles
    :cvar SYR: Syrian Arab Republic
    :cvar TCA: Turks and Caicos Islands
    :cvar TCD: Republic of Chad
    :cvar TGO: Togolese Republic
    :cvar THA: Kingdom of Thailand
    :cvar TJK: Republic of Tajikistan
    :cvar TKL: Tokelau
    :cvar TKM: Turkmenistan
    :cvar TLS: Democratic Republic of Timor-Leste
    :cvar TON: Kingdom of Tonga
    :cvar TTO: Republic of Trinidad and Tobago
    :cvar TUN: Republic of Tunisia
    :cvar TUR: Republic of Turkey
    :cvar TUV: Tuvalu
    :cvar TWN: Taiwan
    :cvar TZA: United Republic of Tanzania
    :cvar UGA: Republic of Uganda
    :cvar UKR: Ukraine
    :cvar URY: Oriental Republic of Uruguay
    :cvar UZB: Republic of Uzbekistan
    :cvar VAT: State of the Vatican City
    :cvar VCT: Saint Vincent and the Grenadines
    :cvar VEN: Bolivarian Republic of Venezuela
    :cvar VGB: British Virgin Islands
    :cvar VIR: United States Virgin Islands
    :cvar VNM: Socialist Republic of Vietnam
    :cvar VUT: Republic of Vanuatu
    :cvar WLF: Wallis and Futuna
    :cvar WSM: Independent State of Samoa
    :cvar XAC: Territory of Ashmore and Cartier Islands
    :cvar XAZ: Entity 1
    :cvar XBI: Bassas da India
    :cvar XBK: Baker Island
    :cvar XCR: Entity 2
    :cvar XCS: Coral Sea Islands Territory
    :cvar XCY: Entity 3
    :cvar XEU: Europa Island
    :cvar XGL: Glorioso Islands
    :cvar XGZ: Gaza Strip
    :cvar XHO: Howland Island
    :cvar XJA: Johnston Atoll
    :cvar XJM: Jan Mayen
    :cvar XJN: Juan de Nova Island
    :cvar XJV: Jarvis Island
    :cvar XKM: Entity 4
    :cvar XKN: Entity 5
    :cvar XKR: Kingman Reef
    :cvar XKS: Republic of Kosovo
    :cvar XMW: Midway Islands
    :cvar XNV: Navassa Island
    :cvar XPL: Palmyra Atoll
    :cvar XPR: Paracel Islands
    :cvar XQZ: Akrotiri
    :cvar XSP: Spratly Islands
    :cvar XSV: Svalbard
    :cvar XTR: Tromelin Island
    :cvar XWB: West Bank
    :cvar XWK: Wake Island
    :cvar XXD: Dhekelia
    :cvar YEM: Republic of Yemen
    :cvar ZAF: Republic of South Africa
    :cvar ZMB: Republic of Zambia
    :cvar ZWE: Republic of Zimbabwe
    :cvar ACGU: FOUR EYES
    :cvar AMSP: AFRICOM Multinational Strategic Partners
    :cvar AOSC: Athens Olympics Security Coalition
    :cvar APFS: African Peacekeeping Force Somalia
    :cvar ASEA: Association of Southeast Asian Nations (ASEAN)
    :cvar AUSTRALIA_GROUP: Australia Group
    :cvar BHTF: Boko Haram Task Force
    :cvar BWCS: Biological Weapons Convention States
    :cvar CFCK: Combined Forces Command Korea
    :cvar CFOD: Coalition Forces Odyssey Dawn
    :cvar CFUP: Coalition Forces Unified Protector
    :cvar CLFC: Combined Libya Fusion Cell
    :cvar CMFC: Combined Maritime Forces Central
    :cvar CMFP: Cooperative Maritime Forces Pacific
    :cvar CPMT: Civilian Protection Monitoring Team for Sudan
    :cvar CTOC: Countering Transnational Organized Crime
    :cvar CWCS: Chemical Weapons Convention States
    :cvar ECTF: European Counter-Terrorism Forces
    :cvar EFOR: European Union Stabilization Forces in Bosnia
    :cvar EU: European Union
    :cvar EUDA: European Union DARFUR
    :cvar FRME: Counter Violent Extremist Organizations Framework
        Partners
    :cvar FVEY: FIVE EYES
    :cvar GCCH: Gulf Cooperation Council
    :cvar GCTF: Global Counter-Terrorism Forces
    :cvar GFNX: Global Foreign Terrorist Fighter Network Exchange
    :cvar GMIF: Global Maritime Interception Forces
    :cvar IESC: International Events Security Coalition
    :cvar IMSC: International Maritime Security Construct
    :cvar IMSP: INDOPACOM Multinational Strategic Partners
    :cvar IPMC: INDO PACIFIC Maritime Call
    :cvar IRKS: Inherent Resolve Kinetic Support
    :cvar ISAF: International Security Assistance Force for Afghanistan
    :cvar ISSG: International Syria Support Group
    :cvar KFOR: Stabilization Forces in Kosovo
    :cvar MCFI: Multinational Coalition Forces-Iraq
    :cvar MESF: Middle East Stability Force
    :cvar MGEU: Multinational GEOINT Europe
    :cvar MIFH: Multinational Interim Force Haiti
    :cvar MLEC: Multi-Lateral Enduring Contingency
    :cvar MNTF: Multinational Task Force
    :cvar MPFL: Multinational Peacekeeping Forces
    :cvar NACT: North African Counter-Terrorism Forces
    :cvar NATO: North Atlantic Treaty Organization
    :cvar NCFE: NATO CFE Treaty on Conventional Armed Forces in Europe
    :cvar NKIC: North Korea Intelligence Coalition
    :cvar NRDC: NORDIC
    :cvar NSG: Nuclear Suppliers' Group
    :cvar OSAG: Olympic Security Advisory Group
    :cvar OSTY: Open Skies Treaty
    :cvar PAWA: Partnership for Actions in West Africa
    :cvar PGMF: Persian Gulf Multinational Forces
    :cvar PSMX: Pacific Security Monitoring Exchange
    :cvar RISC: Russia Intelligence Sharing Coalition
    :cvar RSMA: Resolute Support Mission Afghanistan
    :cvar SFOR: Stabilization Force
    :cvar SOFP: Special Operations Forces Partners
    :cvar SPAA: SOF Planning Activities in Afghanistan (also called
        "11-Eyes")
    :cvar TEYE: THREE EYES
    :cvar TFTC: Terrorist Financing Targeting Center
    :cvar UNCK: United Nations Command, Korea
    """

    FGI = "FGI"
    ABW = "ABW"
    AFG = "AFG"
    AGO = "AGO"
    AIA = "AIA"
    ALB = "ALB"
    AND = "AND"
    ARE = "ARE"
    ARG = "ARG"
    ARM = "ARM"
    ASM = "ASM"
    ATA = "ATA"
    ATF = "ATF"
    ATG = "ATG"
    AUS = "AUS"
    AUT = "AUT"
    AX2 = "AX2"
    AX3 = "AX3"
    AZE = "AZE"
    BDI = "BDI"
    BEL = "BEL"
    BEN = "BEN"
    BES = "BES"
    BFA = "BFA"
    BGD = "BGD"
    BGR = "BGR"
    BHR = "BHR"
    BHS = "BHS"
    BIH = "BIH"
    BLM = "BLM"
    BLR = "BLR"
    BLZ = "BLZ"
    BMU = "BMU"
    BOL = "BOL"
    BRA = "BRA"
    BRB = "BRB"
    BRN = "BRN"
    BTN = "BTN"
    BVT = "BVT"
    BWA = "BWA"
    CAF = "CAF"
    CAN = "CAN"
    CCK = "CCK"
    CHE = "CHE"
    CHL = "CHL"
    CHN = "CHN"
    CIV = "CIV"
    CMR = "CMR"
    COD = "COD"
    COG = "COG"
    COK = "COK"
    COL = "COL"
    COM = "COM"
    CPT = "CPT"
    CPV = "CPV"
    CRI = "CRI"
    CUB = "CUB"
    CUW = "CUW"
    CXR = "CXR"
    CYM = "CYM"
    CYP = "CYP"
    CZE = "CZE"
    DEU = "DEU"
    DGA = "DGA"
    DJI = "DJI"
    DMA = "DMA"
    DNK = "DNK"
    DOM = "DOM"
    DZA = "DZA"
    ECU = "ECU"
    EGY = "EGY"
    ERI = "ERI"
    ESH = "ESH"
    ESP = "ESP"
    EST = "EST"
    ETH = "ETH"
    FIN = "FIN"
    FJI = "FJI"
    FLK = "FLK"
    FRA = "FRA"
    FRO = "FRO"
    FSM = "FSM"
    GAB = "GAB"
    GBR = "GBR"
    GEO = "GEO"
    GGY = "GGY"
    GHA = "GHA"
    GIB = "GIB"
    GIN = "GIN"
    GLP = "GLP"
    GMB = "GMB"
    GNB = "GNB"
    GNQ = "GNQ"
    GRC = "GRC"
    GRD = "GRD"
    GRL = "GRL"
    GTM = "GTM"
    GUF = "GUF"
    GUM = "GUM"
    GUY = "GUY"
    HKG = "HKG"
    HMD = "HMD"
    HND = "HND"
    HRV = "HRV"
    HTI = "HTI"
    HUN = "HUN"
    IDN = "IDN"
    IMN = "IMN"
    IND = "IND"
    IOT = "IOT"
    IRL = "IRL"
    IRN = "IRN"
    IRQ = "IRQ"
    ISL = "ISL"
    ISR = "ISR"
    ITA = "ITA"
    JAM = "JAM"
    JEY = "JEY"
    JOR = "JOR"
    JPN = "JPN"
    KAZ = "KAZ"
    KEN = "KEN"
    KGZ = "KGZ"
    KHM = "KHM"
    KIR = "KIR"
    KNA = "KNA"
    KOR = "KOR"
    KWT = "KWT"
    LAO = "LAO"
    LBN = "LBN"
    LBR = "LBR"
    LBY = "LBY"
    LCA = "LCA"
    LIE = "LIE"
    LKA = "LKA"
    LSO = "LSO"
    LTU = "LTU"
    LUX = "LUX"
    LVA = "LVA"
    MAC = "MAC"
    MAF = "MAF"
    MAR = "MAR"
    MCO = "MCO"
    MDA = "MDA"
    MDG = "MDG"
    MDV = "MDV"
    MEX = "MEX"
    MHL = "MHL"
    MKD = "MKD"
    MLI = "MLI"
    MLT = "MLT"
    MMR = "MMR"
    MNE = "MNE"
    MNG = "MNG"
    MNP = "MNP"
    MOZ = "MOZ"
    MRT = "MRT"
    MSR = "MSR"
    MTQ = "MTQ"
    MUS = "MUS"
    MWI = "MWI"
    MYS = "MYS"
    MYT = "MYT"
    NAM = "NAM"
    NCL = "NCL"
    NER = "NER"
    NFK = "NFK"
    NGA = "NGA"
    NIC = "NIC"
    NIU = "NIU"
    NLD = "NLD"
    NOR = "NOR"
    NPL = "NPL"
    NRU = "NRU"
    NZL = "NZL"
    OMN = "OMN"
    PAK = "PAK"
    PAN = "PAN"
    PCN = "PCN"
    PER = "PER"
    PHL = "PHL"
    PLW = "PLW"
    PNG = "PNG"
    POL = "POL"
    PRI = "PRI"
    PRK = "PRK"
    PRT = "PRT"
    PRY = "PRY"
    PYF = "PYF"
    QAT = "QAT"
    REU = "REU"
    ROU = "ROU"
    RUS = "RUS"
    RWA = "RWA"
    SAU = "SAU"
    SDN = "SDN"
    SEN = "SEN"
    SGP = "SGP"
    SGS = "SGS"
    SHN = "SHN"
    SLB = "SLB"
    SLE = "SLE"
    SLV = "SLV"
    SMR = "SMR"
    SOM = "SOM"
    SPM = "SPM"
    SRB = "SRB"
    SSD = "SSD"
    STP = "STP"
    SUR = "SUR"
    SVK = "SVK"
    SVN = "SVN"
    SWE = "SWE"
    SWZ = "SWZ"
    SXM = "SXM"
    SYC = "SYC"
    SYR = "SYR"
    TCA = "TCA"
    TCD = "TCD"
    TGO = "TGO"
    THA = "THA"
    TJK = "TJK"
    TKL = "TKL"
    TKM = "TKM"
    TLS = "TLS"
    TON = "TON"
    TTO = "TTO"
    TUN = "TUN"
    TUR = "TUR"
    TUV = "TUV"
    TWN = "TWN"
    TZA = "TZA"
    UGA = "UGA"
    UKR = "UKR"
    URY = "URY"
    UZB = "UZB"
    VAT = "VAT"
    VCT = "VCT"
    VEN = "VEN"
    VGB = "VGB"
    VIR = "VIR"
    VNM = "VNM"
    VUT = "VUT"
    WLF = "WLF"
    WSM = "WSM"
    XAC = "XAC"
    XAZ = "XAZ"
    XBI = "XBI"
    XBK = "XBK"
    XCR = "XCR"
    XCS = "XCS"
    XCY = "XCY"
    XEU = "XEU"
    XGL = "XGL"
    XGZ = "XGZ"
    XHO = "XHO"
    XJA = "XJA"
    XJM = "XJM"
    XJN = "XJN"
    XJV = "XJV"
    XKM = "XKM"
    XKN = "XKN"
    XKR = "XKR"
    XKS = "XKS"
    XMW = "XMW"
    XNV = "XNV"
    XPL = "XPL"
    XPR = "XPR"
    XQZ = "XQZ"
    XSP = "XSP"
    XSV = "XSV"
    XTR = "XTR"
    XWB = "XWB"
    XWK = "XWK"
    XXD = "XXD"
    YEM = "YEM"
    ZAF = "ZAF"
    ZMB = "ZMB"
    ZWE = "ZWE"
    ACGU = "ACGU"
    AMSP = "AMSP"
    AOSC = "AOSC"
    APFS = "APFS"
    ASEA = "ASEA"
    AUSTRALIA_GROUP = "AUSTRALIA_GROUP"
    BHTF = "BHTF"
    BWCS = "BWCS"
    CFCK = "CFCK"
    CFOD = "CFOD"
    CFUP = "CFUP"
    CLFC = "CLFC"
    CMFC = "CMFC"
    CMFP = "CMFP"
    CPMT = "CPMT"
    CTOC = "CTOC"
    CWCS = "CWCS"
    ECTF = "ECTF"
    EFOR = "EFOR"
    EU = "EU"
    EUDA = "EUDA"
    FRME = "FRME"
    FVEY = "FVEY"
    GCCH = "GCCH"
    GCTF = "GCTF"
    GFNX = "GFNX"
    GMIF = "GMIF"
    IESC = "IESC"
    IMSC = "IMSC"
    IMSP = "IMSP"
    IPMC = "IPMC"
    IRKS = "IRKS"
    ISAF = "ISAF"
    ISSG = "ISSG"
    KFOR = "KFOR"
    MCFI = "MCFI"
    MESF = "MESF"
    MGEU = "MGEU"
    MIFH = "MIFH"
    MLEC = "MLEC"
    MNTF = "MNTF"
    MPFL = "MPFL"
    NACT = "NACT"
    NATO = "NATO"
    NCFE = "NCFE"
    NKIC = "NKIC"
    NRDC = "NRDC"
    NSG = "NSG"
    OSAG = "OSAG"
    OSTY = "OSTY"
    PAWA = "PAWA"
    PGMF = "PGMF"
    PSMX = "PSMX"
    RISC = "RISC"
    RSMA = "RSMA"
    SFOR = "SFOR"
    SOFP = "SOFP"
    SPAA = "SPAA"
    TEYE = "TEYE"
    TFTC = "TFTC"
    UNCK = "UNCK"


class HighWaterNatoEnum(Enum):
    """
    (U) The highest classification of any portion that has either
    OwnerProducer contains NATO or FGI_SourceOpen contains NATO.

    The HighWaterNATO attribute will be compared against an entity's
    fineAccessControls NATO value. PERMISSIBLE VALUES The permissible
    values for this simple type are defined in the Controlled Value
    Enumeration: CVEnumISMHighWaterNATO.xml.

    :cvar NATO_U: NATO UNCLASSIFIED
    :cvar NATO_R: NATO RESTRICTED
    :cvar NATO_C: NATO CONFIDENTIAL
    :cvar NATO_S: NATO SECRET
    :cvar NATO_TS: NATO TOP SECRET
    """

    NATO_U = "NATO_U"
    NATO_R = "NATO_R"
    NATO_C = "NATO_C"
    NATO_S = "NATO_S"
    NATO_TS = "NATO_TS"


class NonIcMarkingsEnum(Enum):
    """
    (U) All currently valid Non-IC markings from the published register.

    PERMISSIBLE VALUES The permissible values for this simple type are
    defined in the Controlled Value Enumeration: CVEnumISMNonIC.xml.

    :cvar DS: LIMITED DISTRIBUTION
    :cvar XD: EXCLUSIVE DISTRIBUTION
    :cvar ND: NO DISTRIBUTION
    :cvar SBU: SENSITIVE BUT UNCLASSIFIED
    :cvar SBU_NF: SENSITIVE BUT UNCLASSIFIED NOFORN
    :cvar LES: LAW ENFORCEMENT SENSITIVE
    :cvar LES_NF: LAW ENFORCEMENT SENSITIVE NOFORN
    :cvar SSI: SENSITIVE SECURITY INFORMATION
    :cvar NNPI: NAVAL NUCLEAR PROPULSION INFORMATION
    """

    DS = "DS"
    XD = "XD"
    ND = "ND"
    SBU = "SBU"
    SBU_NF = "SBU_NF"
    LES = "LES"
    LES_NF = "LES_NF"
    SSI = "SSI"
    NNPI = "NNPI"


class NonUsControlsEnum(Enum):
    """
    (U) NonUS Control markings supported by ISM PERMISSIBLE VALUES The
    permissible values for this simple type are defined in the Controlled
    Value Enumeration: CVEnumISMNonUSControls.xml.

    :cvar NATO_ATOMAL: NATO Atomal mark
    :cvar NATO_BOHEMIA: NATO Bohemia mark
    :cvar NATO_BALK: NATO Balk mark
    """

    NATO_ATOMAL = "NATO_ATOMAL"
    NATO_BOHEMIA = "NATO_BOHEMIA"
    NATO_BALK = "NATO_BALK"


class OwnerProducerEnum(Enum):
    """
    CVEnumISMCATOwnerProducer Values.

    :cvar FGI: Foreign Government Information
    :cvar ABW: Aruba
    :cvar AFG: Islamic Republic of Afghanistan
    :cvar AGO: Republic of Angola
    :cvar AIA: Anguilla
    :cvar ALB: Republic of Albania
    :cvar AND: Principality of Andorra
    :cvar ARE: United Arab Emirates
    :cvar ARG: Argentine Republic
    :cvar ARM: Republic of Armenia
    :cvar ASM: Territory of American Samoa
    :cvar ATA: Antarctica
    :cvar ATF: French Southern and Antarctic Lands
    :cvar ATG: Antigua and Barbuda
    :cvar AUS: Commonwealth of Australia
    :cvar AUT: Republic of Austria
    :cvar AX2: Guantanamo Bay Naval Base
    :cvar AX3: Entity 6
    :cvar AZE: Republic of Azerbaijan
    :cvar BDI: Republic of Burundi
    :cvar BEL: Kingdom of Belgium
    :cvar BEN: Republic of Benin
    :cvar BES: Bonaire, Sint Eustatius, and Saba
    :cvar BFA: Burkina Faso
    :cvar BGD: People's Republic of Bangladesh
    :cvar BGR: Republic of Bulgaria
    :cvar BHR: Kingdom of Bahrain
    :cvar BHS: Commonwealth of The Bahamas
    :cvar BIH: Bosnia and Herzegovina
    :cvar BLM: Saint Barthelemy
    :cvar BLR: Republic of Belarus
    :cvar BLZ: Belize
    :cvar BMU: Bermuda
    :cvar BOL: Plurinational State of Bolivia
    :cvar BRA: Federative Republic of Brazil
    :cvar BRB: Barbados
    :cvar BRN: Brunei Darussalam
    :cvar BTN: Kingdom of Bhutan
    :cvar BVT: Bouvet Island
    :cvar BWA: Republic of Botswana
    :cvar CAF: Central African Republic
    :cvar CAN: Canada
    :cvar CCK: Territory of Cocos (Keeling) Islands
    :cvar CHE: Swiss Confederation
    :cvar CHL: Republic of Chile
    :cvar CHN: People's Republic of China
    :cvar CIV: Republic of Côte d'Ivoire
    :cvar CMR: Republic of Cameroon
    :cvar COD: Democratic Republic of the Congo
    :cvar COG: Republic of the Congo
    :cvar COK: Cook Islands
    :cvar COL: Republic of Colombia
    :cvar COM: Union of the Comoros
    :cvar CPT: Clipperton Island
    :cvar CPV: Republic of Cabo Verde
    :cvar CRI: Republic of Costa Rica
    :cvar CUB: Republic of Cuba
    :cvar CUW: Curaçao
    :cvar CXR: Territory of Christmas Island
    :cvar CYM: Cayman Islands
    :cvar CYP: Republic of Cyprus
    :cvar CZE: Czech Republic
    :cvar DEU: Federal Republic of Germany
    :cvar DGA: Diego Garcia
    :cvar DJI: Republic of Djibouti
    :cvar DMA: Commonwealth of Dominica
    :cvar DNK: Kingdom of Denmark
    :cvar DOM: Dominican Republic
    :cvar DZA: People's Democratic Republic of Algeria
    :cvar ECU: Republic of Ecuador
    :cvar EGY: Arab Republic of Egypt
    :cvar ERI: State of Eritrea
    :cvar ESH: Western Sahara
    :cvar ESP: Kingdom of Spain
    :cvar EST: Republic of Estonia
    :cvar ETH: Federal Democratic Republic of Ethiopia
    :cvar FIN: Republic of Finland
    :cvar FJI: Republic of Fiji
    :cvar FLK: Falkland Islands (Islas Malvinas)
    :cvar FRA: French Republic
    :cvar FRO: Faroe Islands
    :cvar FSM: Federated States of Micronesia
    :cvar GAB: Gabonese Republic
    :cvar GBR: United Kingdom of Great Britain and Northern Ireland
    :cvar GEO: Georgia
    :cvar GGY: Bailiwick of Guernsey
    :cvar GHA: Republic of Ghana
    :cvar GIB: Gibraltar
    :cvar GIN: Republic of Guinea
    :cvar GLP: Region of Guadeloupe
    :cvar GMB: Republic of The Gambia
    :cvar GNB: Republic of Guinea-Bissau
    :cvar GNQ: Republic of Equatorial Guinea
    :cvar GRC: Hellenic Republic
    :cvar GRD: Grenada
    :cvar GRL: Greenland
    :cvar GTM: Republic of Guatemala
    :cvar GUF: Territorial Collectivity of Guiana
    :cvar GUM: Territory of Guam
    :cvar GUY: Co-operative Republic of Guyana
    :cvar HKG: Hong Kong Special Administrative Region
    :cvar HMD: Territory of Heard Island and McDonald Islands
    :cvar HND: Republic of Honduras
    :cvar HRV: Republic of Croatia
    :cvar HTI: Republic of Haiti
    :cvar HUN: Hungary
    :cvar IDN: Republic of Indonesia
    :cvar IMN: Isle of Man
    :cvar IND: Republic of India
    :cvar IOT: British Indian Ocean Territory
    :cvar IRL: Ireland
    :cvar IRN: Islamic Republic of Iran
    :cvar IRQ: Republic of Iraq
    :cvar ISL: Republic of Iceland
    :cvar ISR: State of Israel
    :cvar ITA: Italian Republic
    :cvar JAM: Jamaica
    :cvar JEY: Bailiwick of Jersey
    :cvar JOR: Hashemite Kingdom of Jordan
    :cvar JPN: Japan
    :cvar KAZ: Republic of Kazakhstan
    :cvar KEN: Republic of Kenya
    :cvar KGZ: Kyrgyz Republic
    :cvar KHM: Kingdom of Cambodia
    :cvar KIR: Republic of Kiribati
    :cvar KNA: Federation of Saint Kitts and Nevis
    :cvar KOR: Republic of Korea
    :cvar KWT: State of Kuwait
    :cvar LAO: Lao People's Democratic Republic
    :cvar LBN: Lebanese Republic
    :cvar LBR: Republic of Liberia
    :cvar LBY: State of Libya
    :cvar LCA: Saint Lucia
    :cvar LIE: Principality of Liechtenstein
    :cvar LKA: Democratic Socialist Republic of Sri Lanka
    :cvar LSO: Kingdom of Lesotho
    :cvar LTU: Republic of Lithuania
    :cvar LUX: Grand Duchy of Luxembourg
    :cvar LVA: Republic of Latvia
    :cvar MAC: Macau Special Administrative Region
    :cvar MAF: Saint Martin
    :cvar MAR: Kingdom of Morocco
    :cvar MCO: Principality of Monaco
    :cvar MDA: Republic of Moldova
    :cvar MDG: Republic of Madagascar
    :cvar MDV: Republic of Maldives
    :cvar MEX: United Mexican States
    :cvar MHL: Republic of the Marshall Islands
    :cvar MKD: Republic of North Macedonia
    :cvar MLI: Republic of Mali
    :cvar MLT: Republic of Malta
    :cvar MMR: Union of Burma
    :cvar MNE: Montenegro
    :cvar MNG: Mongolia
    :cvar MNP: Commonwealth of the Northern Mariana Islands
    :cvar MOZ: Republic of Mozambique
    :cvar MRT: Islamic Republic of Mauritania
    :cvar MSR: Montserrat
    :cvar MTQ: Territorial Collectivity of Martinique
    :cvar MUS: Republic of Mauritius
    :cvar MWI: Republic of Malawi
    :cvar MYS: Malaysia
    :cvar MYT: Department of Mayotte
    :cvar NAM: Republic of Namibia
    :cvar NCL: New Caledonia
    :cvar NER: Republic of Niger
    :cvar NFK: Territory of Norfolk Island
    :cvar NGA: Federal Republic of Nigeria
    :cvar NIC: Republic of Nicaragua
    :cvar NIU: Niue
    :cvar NLD: Kingdom of the Netherlands
    :cvar NOR: Kingdom of Norway
    :cvar NPL: Federal Democratic Republic of Nepal
    :cvar NRU: Republic of Nauru
    :cvar NZL: New Zealand
    :cvar OMN: Sultanate of Oman
    :cvar PAK: Islamic Republic of Pakistan
    :cvar PAN: Republic of Panama
    :cvar PCN: Pitcairn, Henderson, Ducie, and Oeno Islands
    :cvar PER: Republic of Peru
    :cvar PHL: Republic of the Philippines
    :cvar PLW: Republic of Palau
    :cvar PNG: Independent State of Papua New Guinea
    :cvar POL: Republic of Poland
    :cvar PRI: Commonwealth of Puerto Rico
    :cvar PRK: Democratic People's Republic of Korea
    :cvar PRT: Portuguese Republic
    :cvar PRY: Republic of Paraguay
    :cvar PYF: French Polynesia
    :cvar QAT: State of Qatar
    :cvar REU: Region of Reunion
    :cvar ROU: Romania
    :cvar RUS: Russian Federation
    :cvar RWA: Republic of Rwanda
    :cvar SAU: Kingdom of Saudi Arabia
    :cvar SDN: Republic of the Sudan
    :cvar SEN: Republic of Senegal
    :cvar SGP: Republic of Singapore
    :cvar SGS: South Georgia and the South Sandwich Islands
    :cvar SHN: Saint Helena, Ascension, and Tristan da Cunha
    :cvar SLB: Solomon Islands
    :cvar SLE: Republic of Sierra Leone
    :cvar SLV: Republic of El Salvador
    :cvar SMR: Republic of San Marino
    :cvar SOM: Federal Republic of Somalia
    :cvar SPM: Territorial Collectivity of Saint Pierre and Miquelon
    :cvar SRB: Republic of Serbia
    :cvar SSD: Republic of South Sudan
    :cvar STP: Democratic Republic of Sao Tome and Principe
    :cvar SUR: Republic of Suriname
    :cvar SVK: Slovak Republic
    :cvar SVN: Republic of Slovenia
    :cvar SWE: Kingdom of Sweden
    :cvar SWZ: Kingdom of Eswatini
    :cvar SXM: Sint Maarten
    :cvar SYC: Republic of Seychelles
    :cvar SYR: Syrian Arab Republic
    :cvar TCA: Turks and Caicos Islands
    :cvar TCD: Republic of Chad
    :cvar TGO: Togolese Republic
    :cvar THA: Kingdom of Thailand
    :cvar TJK: Republic of Tajikistan
    :cvar TKL: Tokelau
    :cvar TKM: Turkmenistan
    :cvar TLS: Democratic Republic of Timor-Leste
    :cvar TON: Kingdom of Tonga
    :cvar TTO: Republic of Trinidad and Tobago
    :cvar TUN: Republic of Tunisia
    :cvar TUR: Republic of Turkey
    :cvar TUV: Tuvalu
    :cvar TWN: Taiwan
    :cvar TZA: United Republic of Tanzania
    :cvar UGA: Republic of Uganda
    :cvar UKR: Ukraine
    :cvar URY: Oriental Republic of Uruguay
    :cvar USA: United States of America
    :cvar UZB: Republic of Uzbekistan
    :cvar VAT: State of the Vatican City
    :cvar VCT: Saint Vincent and the Grenadines
    :cvar VEN: Bolivarian Republic of Venezuela
    :cvar VGB: British Virgin Islands
    :cvar VIR: United States Virgin Islands
    :cvar VNM: Socialist Republic of Vietnam
    :cvar VUT: Republic of Vanuatu
    :cvar WLF: Wallis and Futuna
    :cvar WSM: Independent State of Samoa
    :cvar XAC: Territory of Ashmore and Cartier Islands
    :cvar XAZ: Entity 1
    :cvar XBI: Bassas da India
    :cvar XBK: Baker Island
    :cvar XCR: Entity 2
    :cvar XCS: Coral Sea Islands Territory
    :cvar XCY: Entity 3
    :cvar XEU: Europa Island
    :cvar XGL: Glorioso Islands
    :cvar XGZ: Gaza Strip
    :cvar XHO: Howland Island
    :cvar XJA: Johnston Atoll
    :cvar XJM: Jan Mayen
    :cvar XJN: Juan de Nova Island
    :cvar XJV: Jarvis Island
    :cvar XKM: Entity 4
    :cvar XKN: Entity 5
    :cvar XKR: Kingman Reef
    :cvar XKS: Republic of Kosovo
    :cvar XMW: Midway Islands
    :cvar XNV: Navassa Island
    :cvar XPL: Palmyra Atoll
    :cvar XPR: Paracel Islands
    :cvar XQZ: Akrotiri
    :cvar XSP: Spratly Islands
    :cvar XSV: Svalbard
    :cvar XTR: Tromelin Island
    :cvar XWB: West Bank
    :cvar XWK: Wake Island
    :cvar XXD: Dhekelia
    :cvar YEM: Republic of Yemen
    :cvar ZAF: Republic of South Africa
    :cvar ZMB: Republic of Zambia
    :cvar ZWE: Republic of Zimbabwe
    :cvar ACGU: FOUR EYES
    :cvar AMSP: AFRICOM Multinational Strategic Partners
    :cvar AOSC: Athens Olympics Security Coalition
    :cvar APFS: African Peacekeeping Force Somalia
    :cvar ASEA: Association of Southeast Asian Nations (ASEAN)
    :cvar AUSTRALIA_GROUP: Australia Group
    :cvar BHTF: Boko Haram Task Force
    :cvar BWCS: Biological Weapons Convention States
    :cvar CFCK: Combined Forces Command Korea
    :cvar CFOD: Coalition Forces Odyssey Dawn
    :cvar CFUP: Coalition Forces Unified Protector
    :cvar CLFC: Combined Libya Fusion Cell
    :cvar CMFC: Combined Maritime Forces Central
    :cvar CMFP: Cooperative Maritime Forces Pacific
    :cvar CPMT: Civilian Protection Monitoring Team for Sudan
    :cvar CTOC: Countering Transnational Organized Crime
    :cvar CWCS: Chemical Weapons Convention States
    :cvar ECTF: European Counter-Terrorism Forces
    :cvar EFOR: European Union Stabilization Forces in Bosnia
    :cvar EU: European Union
    :cvar EUDA: European Union DARFUR
    :cvar FRME: Counter Violent Extremist Organizations Framework
        Partners
    :cvar FVEY: FIVE EYES
    :cvar GCCH: Gulf Cooperation Council
    :cvar GCTF: Global Counter-Terrorism Forces
    :cvar GFNX: Global Foreign Terrorist Fighter Network Exchange
    :cvar GMIF: Global Maritime Interception Forces
    :cvar IESC: International Events Security Coalition
    :cvar IMSC: International Maritime Security Construct
    :cvar IMSP: INDOPACOM Multinational Strategic Partners
    :cvar IPMC: INDO PACIFIC Maritime Call
    :cvar IRKS: Inherent Resolve Kinetic Support
    :cvar ISAF: International Security Assistance Force for Afghanistan
    :cvar ISSG: International Syria Support Group
    :cvar KFOR: Stabilization Forces in Kosovo
    :cvar MCFI: Multinational Coalition Forces-Iraq
    :cvar MESF: Middle East Stability Force
    :cvar MGEU: Multinational GEOINT Europe
    :cvar MIFH: Multinational Interim Force Haiti
    :cvar MLEC: Multi-Lateral Enduring Contingency
    :cvar MNTF: Multinational Task Force
    :cvar MPFL: Multinational Peacekeeping Forces
    :cvar NACT: North African Counter-Terrorism Forces
    :cvar NATO: North Atlantic Treaty Organization
    :cvar NCFE: NATO CFE Treaty on Conventional Armed Forces in Europe
    :cvar NKIC: North Korea Intelligence Coalition
    :cvar NRDC: NORDIC
    :cvar NSG: Nuclear Suppliers' Group
    :cvar OSAG: Olympic Security Advisory Group
    :cvar OSTY: Open Skies Treaty
    :cvar PAWA: Partnership for Actions in West Africa
    :cvar PGMF: Persian Gulf Multinational Forces
    :cvar PSMX: Pacific Security Monitoring Exchange
    :cvar RISC: Russia Intelligence Sharing Coalition
    :cvar RSMA: Resolute Support Mission Afghanistan
    :cvar SFOR: Stabilization Force
    :cvar SOFP: Special Operations Forces Partners
    :cvar SPAA: SOF Planning Activities in Afghanistan (also called
        "11-Eyes")
    :cvar TEYE: THREE EYES
    :cvar TFTC: Terrorist Financing Targeting Center
    :cvar UNCK: United Nations Command, Korea
    """

    FGI = "FGI"
    ABW = "ABW"
    AFG = "AFG"
    AGO = "AGO"
    AIA = "AIA"
    ALB = "ALB"
    AND = "AND"
    ARE = "ARE"
    ARG = "ARG"
    ARM = "ARM"
    ASM = "ASM"
    ATA = "ATA"
    ATF = "ATF"
    ATG = "ATG"
    AUS = "AUS"
    AUT = "AUT"
    AX2 = "AX2"
    AX3 = "AX3"
    AZE = "AZE"
    BDI = "BDI"
    BEL = "BEL"
    BEN = "BEN"
    BES = "BES"
    BFA = "BFA"
    BGD = "BGD"
    BGR = "BGR"
    BHR = "BHR"
    BHS = "BHS"
    BIH = "BIH"
    BLM = "BLM"
    BLR = "BLR"
    BLZ = "BLZ"
    BMU = "BMU"
    BOL = "BOL"
    BRA = "BRA"
    BRB = "BRB"
    BRN = "BRN"
    BTN = "BTN"
    BVT = "BVT"
    BWA = "BWA"
    CAF = "CAF"
    CAN = "CAN"
    CCK = "CCK"
    CHE = "CHE"
    CHL = "CHL"
    CHN = "CHN"
    CIV = "CIV"
    CMR = "CMR"
    COD = "COD"
    COG = "COG"
    COK = "COK"
    COL = "COL"
    COM = "COM"
    CPT = "CPT"
    CPV = "CPV"
    CRI = "CRI"
    CUB = "CUB"
    CUW = "CUW"
    CXR = "CXR"
    CYM = "CYM"
    CYP = "CYP"
    CZE = "CZE"
    DEU = "DEU"
    DGA = "DGA"
    DJI = "DJI"
    DMA = "DMA"
    DNK = "DNK"
    DOM = "DOM"
    DZA = "DZA"
    ECU = "ECU"
    EGY = "EGY"
    ERI = "ERI"
    ESH = "ESH"
    ESP = "ESP"
    EST = "EST"
    ETH = "ETH"
    FIN = "FIN"
    FJI = "FJI"
    FLK = "FLK"
    FRA = "FRA"
    FRO = "FRO"
    FSM = "FSM"
    GAB = "GAB"
    GBR = "GBR"
    GEO = "GEO"
    GGY = "GGY"
    GHA = "GHA"
    GIB = "GIB"
    GIN = "GIN"
    GLP = "GLP"
    GMB = "GMB"
    GNB = "GNB"
    GNQ = "GNQ"
    GRC = "GRC"
    GRD = "GRD"
    GRL = "GRL"
    GTM = "GTM"
    GUF = "GUF"
    GUM = "GUM"
    GUY = "GUY"
    HKG = "HKG"
    HMD = "HMD"
    HND = "HND"
    HRV = "HRV"
    HTI = "HTI"
    HUN = "HUN"
    IDN = "IDN"
    IMN = "IMN"
    IND = "IND"
    IOT = "IOT"
    IRL = "IRL"
    IRN = "IRN"
    IRQ = "IRQ"
    ISL = "ISL"
    ISR = "ISR"
    ITA = "ITA"
    JAM = "JAM"
    JEY = "JEY"
    JOR = "JOR"
    JPN = "JPN"
    KAZ = "KAZ"
    KEN = "KEN"
    KGZ = "KGZ"
    KHM = "KHM"
    KIR = "KIR"
    KNA = "KNA"
    KOR = "KOR"
    KWT = "KWT"
    LAO = "LAO"
    LBN = "LBN"
    LBR = "LBR"
    LBY = "LBY"
    LCA = "LCA"
    LIE = "LIE"
    LKA = "LKA"
    LSO = "LSO"
    LTU = "LTU"
    LUX = "LUX"
    LVA = "LVA"
    MAC = "MAC"
    MAF = "MAF"
    MAR = "MAR"
    MCO = "MCO"
    MDA = "MDA"
    MDG = "MDG"
    MDV = "MDV"
    MEX = "MEX"
    MHL = "MHL"
    MKD = "MKD"
    MLI = "MLI"
    MLT = "MLT"
    MMR = "MMR"
    MNE = "MNE"
    MNG = "MNG"
    MNP = "MNP"
    MOZ = "MOZ"
    MRT = "MRT"
    MSR = "MSR"
    MTQ = "MTQ"
    MUS = "MUS"
    MWI = "MWI"
    MYS = "MYS"
    MYT = "MYT"
    NAM = "NAM"
    NCL = "NCL"
    NER = "NER"
    NFK = "NFK"
    NGA = "NGA"
    NIC = "NIC"
    NIU = "NIU"
    NLD = "NLD"
    NOR = "NOR"
    NPL = "NPL"
    NRU = "NRU"
    NZL = "NZL"
    OMN = "OMN"
    PAK = "PAK"
    PAN = "PAN"
    PCN = "PCN"
    PER = "PER"
    PHL = "PHL"
    PLW = "PLW"
    PNG = "PNG"
    POL = "POL"
    PRI = "PRI"
    PRK = "PRK"
    PRT = "PRT"
    PRY = "PRY"
    PYF = "PYF"
    QAT = "QAT"
    REU = "REU"
    ROU = "ROU"
    RUS = "RUS"
    RWA = "RWA"
    SAU = "SAU"
    SDN = "SDN"
    SEN = "SEN"
    SGP = "SGP"
    SGS = "SGS"
    SHN = "SHN"
    SLB = "SLB"
    SLE = "SLE"
    SLV = "SLV"
    SMR = "SMR"
    SOM = "SOM"
    SPM = "SPM"
    SRB = "SRB"
    SSD = "SSD"
    STP = "STP"
    SUR = "SUR"
    SVK = "SVK"
    SVN = "SVN"
    SWE = "SWE"
    SWZ = "SWZ"
    SXM = "SXM"
    SYC = "SYC"
    SYR = "SYR"
    TCA = "TCA"
    TCD = "TCD"
    TGO = "TGO"
    THA = "THA"
    TJK = "TJK"
    TKL = "TKL"
    TKM = "TKM"
    TLS = "TLS"
    TON = "TON"
    TTO = "TTO"
    TUN = "TUN"
    TUR = "TUR"
    TUV = "TUV"
    TWN = "TWN"
    TZA = "TZA"
    UGA = "UGA"
    UKR = "UKR"
    URY = "URY"
    USA = "USA"
    UZB = "UZB"
    VAT = "VAT"
    VCT = "VCT"
    VEN = "VEN"
    VGB = "VGB"
    VIR = "VIR"
    VNM = "VNM"
    VUT = "VUT"
    WLF = "WLF"
    WSM = "WSM"
    XAC = "XAC"
    XAZ = "XAZ"
    XBI = "XBI"
    XBK = "XBK"
    XCR = "XCR"
    XCS = "XCS"
    XCY = "XCY"
    XEU = "XEU"
    XGL = "XGL"
    XGZ = "XGZ"
    XHO = "XHO"
    XJA = "XJA"
    XJM = "XJM"
    XJN = "XJN"
    XJV = "XJV"
    XKM = "XKM"
    XKN = "XKN"
    XKR = "XKR"
    XKS = "XKS"
    XMW = "XMW"
    XNV = "XNV"
    XPL = "XPL"
    XPR = "XPR"
    XQZ = "XQZ"
    XSP = "XSP"
    XSV = "XSV"
    XTR = "XTR"
    XWB = "XWB"
    XWK = "XWK"
    XXD = "XXD"
    YEM = "YEM"
    ZAF = "ZAF"
    ZMB = "ZMB"
    ZWE = "ZWE"
    ACGU = "ACGU"
    AMSP = "AMSP"
    AOSC = "AOSC"
    APFS = "APFS"
    ASEA = "ASEA"
    AUSTRALIA_GROUP = "AUSTRALIA_GROUP"
    BHTF = "BHTF"
    BWCS = "BWCS"
    CFCK = "CFCK"
    CFOD = "CFOD"
    CFUP = "CFUP"
    CLFC = "CLFC"
    CMFC = "CMFC"
    CMFP = "CMFP"
    CPMT = "CPMT"
    CTOC = "CTOC"
    CWCS = "CWCS"
    ECTF = "ECTF"
    EFOR = "EFOR"
    EU = "EU"
    EUDA = "EUDA"
    FRME = "FRME"
    FVEY = "FVEY"
    GCCH = "GCCH"
    GCTF = "GCTF"
    GFNX = "GFNX"
    GMIF = "GMIF"
    IESC = "IESC"
    IMSC = "IMSC"
    IMSP = "IMSP"
    IPMC = "IPMC"
    IRKS = "IRKS"
    ISAF = "ISAF"
    ISSG = "ISSG"
    KFOR = "KFOR"
    MCFI = "MCFI"
    MESF = "MESF"
    MGEU = "MGEU"
    MIFH = "MIFH"
    MLEC = "MLEC"
    MNTF = "MNTF"
    MPFL = "MPFL"
    NACT = "NACT"
    NATO = "NATO"
    NCFE = "NCFE"
    NKIC = "NKIC"
    NRDC = "NRDC"
    NSG = "NSG"
    OSAG = "OSAG"
    OSTY = "OSTY"
    PAWA = "PAWA"
    PGMF = "PGMF"
    PSMX = "PSMX"
    RISC = "RISC"
    RSMA = "RSMA"
    SFOR = "SFOR"
    SOFP = "SOFP"
    SPAA = "SPAA"
    TEYE = "TEYE"
    TFTC = "TFTC"
    UNCK = "UNCK"


class ReleasableToEnum(Enum):
    """
    CVEnumISMCATRelTo Values.

    :cvar USA: United States of America
    :cvar ABW: Aruba
    :cvar AFG: Islamic Republic of Afghanistan
    :cvar AGO: Republic of Angola
    :cvar AIA: Anguilla
    :cvar ALB: Republic of Albania
    :cvar AND: Principality of Andorra
    :cvar ARE: United Arab Emirates
    :cvar ARG: Argentine Republic
    :cvar ARM: Republic of Armenia
    :cvar ASM: Territory of American Samoa
    :cvar ATA: Antarctica
    :cvar ATF: French Southern and Antarctic Lands
    :cvar ATG: Antigua and Barbuda
    :cvar AUS: Commonwealth of Australia
    :cvar AUT: Republic of Austria
    :cvar AX2: Guantanamo Bay Naval Base
    :cvar AX3: Entity 6
    :cvar AZE: Republic of Azerbaijan
    :cvar BDI: Republic of Burundi
    :cvar BEL: Kingdom of Belgium
    :cvar BEN: Republic of Benin
    :cvar BES: Bonaire, Sint Eustatius, and Saba
    :cvar BFA: Burkina Faso
    :cvar BGD: People's Republic of Bangladesh
    :cvar BGR: Republic of Bulgaria
    :cvar BHR: Kingdom of Bahrain
    :cvar BHS: Commonwealth of The Bahamas
    :cvar BIH: Bosnia and Herzegovina
    :cvar BLM: Saint Barthelemy
    :cvar BLR: Republic of Belarus
    :cvar BLZ: Belize
    :cvar BMU: Bermuda
    :cvar BOL: Plurinational State of Bolivia
    :cvar BRA: Federative Republic of Brazil
    :cvar BRB: Barbados
    :cvar BRN: Brunei Darussalam
    :cvar BTN: Kingdom of Bhutan
    :cvar BVT: Bouvet Island
    :cvar BWA: Republic of Botswana
    :cvar CAF: Central African Republic
    :cvar CAN: Canada
    :cvar CCK: Territory of Cocos (Keeling) Islands
    :cvar CHE: Swiss Confederation
    :cvar CHL: Republic of Chile
    :cvar CHN: People's Republic of China
    :cvar CIV: Republic of Côte d'Ivoire
    :cvar CMR: Republic of Cameroon
    :cvar COD: Democratic Republic of the Congo
    :cvar COG: Republic of the Congo
    :cvar COK: Cook Islands
    :cvar COL: Republic of Colombia
    :cvar COM: Union of the Comoros
    :cvar CPT: Clipperton Island
    :cvar CPV: Republic of Cabo Verde
    :cvar CRI: Republic of Costa Rica
    :cvar CUB: Republic of Cuba
    :cvar CUW: Curaçao
    :cvar CXR: Territory of Christmas Island
    :cvar CYM: Cayman Islands
    :cvar CYP: Republic of Cyprus
    :cvar CZE: Czech Republic
    :cvar DEU: Federal Republic of Germany
    :cvar DGA: Diego Garcia
    :cvar DJI: Republic of Djibouti
    :cvar DMA: Commonwealth of Dominica
    :cvar DNK: Kingdom of Denmark
    :cvar DOM: Dominican Republic
    :cvar DZA: People's Democratic Republic of Algeria
    :cvar ECU: Republic of Ecuador
    :cvar EGY: Arab Republic of Egypt
    :cvar ERI: State of Eritrea
    :cvar ESH: Western Sahara
    :cvar ESP: Kingdom of Spain
    :cvar EST: Republic of Estonia
    :cvar ETH: Federal Democratic Republic of Ethiopia
    :cvar FIN: Republic of Finland
    :cvar FJI: Republic of Fiji
    :cvar FLK: Falkland Islands (Islas Malvinas)
    :cvar FRA: French Republic
    :cvar FRO: Faroe Islands
    :cvar FSM: Federated States of Micronesia
    :cvar GAB: Gabonese Republic
    :cvar GBR: United Kingdom of Great Britain and Northern Ireland
    :cvar GEO: Georgia
    :cvar GGY: Bailiwick of Guernsey
    :cvar GHA: Republic of Ghana
    :cvar GIB: Gibraltar
    :cvar GIN: Republic of Guinea
    :cvar GLP: Region of Guadeloupe
    :cvar GMB: Republic of The Gambia
    :cvar GNB: Republic of Guinea-Bissau
    :cvar GNQ: Republic of Equatorial Guinea
    :cvar GRC: Hellenic Republic
    :cvar GRD: Grenada
    :cvar GRL: Greenland
    :cvar GTM: Republic of Guatemala
    :cvar GUF: Territorial Collectivity of Guiana
    :cvar GUM: Territory of Guam
    :cvar GUY: Co-operative Republic of Guyana
    :cvar HKG: Hong Kong Special Administrative Region
    :cvar HMD: Territory of Heard Island and McDonald Islands
    :cvar HND: Republic of Honduras
    :cvar HRV: Republic of Croatia
    :cvar HTI: Republic of Haiti
    :cvar HUN: Hungary
    :cvar IDN: Republic of Indonesia
    :cvar IMN: Isle of Man
    :cvar IND: Republic of India
    :cvar IOT: British Indian Ocean Territory
    :cvar IRL: Ireland
    :cvar IRN: Islamic Republic of Iran
    :cvar IRQ: Republic of Iraq
    :cvar ISL: Republic of Iceland
    :cvar ISR: State of Israel
    :cvar ITA: Italian Republic
    :cvar JAM: Jamaica
    :cvar JEY: Bailiwick of Jersey
    :cvar JOR: Hashemite Kingdom of Jordan
    :cvar JPN: Japan
    :cvar KAZ: Republic of Kazakhstan
    :cvar KEN: Republic of Kenya
    :cvar KGZ: Kyrgyz Republic
    :cvar KHM: Kingdom of Cambodia
    :cvar KIR: Republic of Kiribati
    :cvar KNA: Federation of Saint Kitts and Nevis
    :cvar KOR: Republic of Korea
    :cvar KWT: State of Kuwait
    :cvar LAO: Lao People's Democratic Republic
    :cvar LBN: Lebanese Republic
    :cvar LBR: Republic of Liberia
    :cvar LBY: State of Libya
    :cvar LCA: Saint Lucia
    :cvar LIE: Principality of Liechtenstein
    :cvar LKA: Democratic Socialist Republic of Sri Lanka
    :cvar LSO: Kingdom of Lesotho
    :cvar LTU: Republic of Lithuania
    :cvar LUX: Grand Duchy of Luxembourg
    :cvar LVA: Republic of Latvia
    :cvar MAC: Macau Special Administrative Region
    :cvar MAF: Saint Martin
    :cvar MAR: Kingdom of Morocco
    :cvar MCO: Principality of Monaco
    :cvar MDA: Republic of Moldova
    :cvar MDG: Republic of Madagascar
    :cvar MDV: Republic of Maldives
    :cvar MEX: United Mexican States
    :cvar MHL: Republic of the Marshall Islands
    :cvar MKD: Republic of North Macedonia
    :cvar MLI: Republic of Mali
    :cvar MLT: Republic of Malta
    :cvar MMR: Union of Burma
    :cvar MNE: Montenegro
    :cvar MNG: Mongolia
    :cvar MNP: Commonwealth of the Northern Mariana Islands
    :cvar MOZ: Republic of Mozambique
    :cvar MRT: Islamic Republic of Mauritania
    :cvar MSR: Montserrat
    :cvar MTQ: Territorial Collectivity of Martinique
    :cvar MUS: Republic of Mauritius
    :cvar MWI: Republic of Malawi
    :cvar MYS: Malaysia
    :cvar MYT: Department of Mayotte
    :cvar NAM: Republic of Namibia
    :cvar NCL: New Caledonia
    :cvar NER: Republic of Niger
    :cvar NFK: Territory of Norfolk Island
    :cvar NGA: Federal Republic of Nigeria
    :cvar NIC: Republic of Nicaragua
    :cvar NIU: Niue
    :cvar NLD: Kingdom of the Netherlands
    :cvar NOR: Kingdom of Norway
    :cvar NPL: Federal Democratic Republic of Nepal
    :cvar NRU: Republic of Nauru
    :cvar NZL: New Zealand
    :cvar OMN: Sultanate of Oman
    :cvar PAK: Islamic Republic of Pakistan
    :cvar PAN: Republic of Panama
    :cvar PCN: Pitcairn, Henderson, Ducie, and Oeno Islands
    :cvar PER: Republic of Peru
    :cvar PHL: Republic of the Philippines
    :cvar PLW: Republic of Palau
    :cvar PNG: Independent State of Papua New Guinea
    :cvar POL: Republic of Poland
    :cvar PRI: Commonwealth of Puerto Rico
    :cvar PRK: Democratic People's Republic of Korea
    :cvar PRT: Portuguese Republic
    :cvar PRY: Republic of Paraguay
    :cvar PYF: French Polynesia
    :cvar QAT: State of Qatar
    :cvar REU: Region of Reunion
    :cvar ROU: Romania
    :cvar RUS: Russian Federation
    :cvar RWA: Republic of Rwanda
    :cvar SAU: Kingdom of Saudi Arabia
    :cvar SDN: Republic of the Sudan
    :cvar SEN: Republic of Senegal
    :cvar SGP: Republic of Singapore
    :cvar SGS: South Georgia and the South Sandwich Islands
    :cvar SHN: Saint Helena, Ascension, and Tristan da Cunha
    :cvar SLB: Solomon Islands
    :cvar SLE: Republic of Sierra Leone
    :cvar SLV: Republic of El Salvador
    :cvar SMR: Republic of San Marino
    :cvar SOM: Federal Republic of Somalia
    :cvar SPM: Territorial Collectivity of Saint Pierre and Miquelon
    :cvar SRB: Republic of Serbia
    :cvar SSD: Republic of South Sudan
    :cvar STP: Democratic Republic of Sao Tome and Principe
    :cvar SUR: Republic of Suriname
    :cvar SVK: Slovak Republic
    :cvar SVN: Republic of Slovenia
    :cvar SWE: Kingdom of Sweden
    :cvar SWZ: Kingdom of Eswatini
    :cvar SXM: Sint Maarten
    :cvar SYC: Republic of Seychelles
    :cvar SYR: Syrian Arab Republic
    :cvar TCA: Turks and Caicos Islands
    :cvar TCD: Republic of Chad
    :cvar TGO: Togolese Republic
    :cvar THA: Kingdom of Thailand
    :cvar TJK: Republic of Tajikistan
    :cvar TKL: Tokelau
    :cvar TKM: Turkmenistan
    :cvar TLS: Democratic Republic of Timor-Leste
    :cvar TON: Kingdom of Tonga
    :cvar TTO: Republic of Trinidad and Tobago
    :cvar TUN: Republic of Tunisia
    :cvar TUR: Republic of Turkey
    :cvar TUV: Tuvalu
    :cvar TWN: Taiwan
    :cvar TZA: United Republic of Tanzania
    :cvar UGA: Republic of Uganda
    :cvar UKR: Ukraine
    :cvar URY: Oriental Republic of Uruguay
    :cvar UZB: Republic of Uzbekistan
    :cvar VAT: State of the Vatican City
    :cvar VCT: Saint Vincent and the Grenadines
    :cvar VEN: Bolivarian Republic of Venezuela
    :cvar VGB: British Virgin Islands
    :cvar VIR: United States Virgin Islands
    :cvar VNM: Socialist Republic of Vietnam
    :cvar VUT: Republic of Vanuatu
    :cvar WLF: Wallis and Futuna
    :cvar WSM: Independent State of Samoa
    :cvar XAC: Territory of Ashmore and Cartier Islands
    :cvar XAZ: Entity 1
    :cvar XBI: Bassas da India
    :cvar XBK: Baker Island
    :cvar XCR: Entity 2
    :cvar XCS: Coral Sea Islands Territory
    :cvar XCY: Entity 3
    :cvar XEU: Europa Island
    :cvar XGL: Glorioso Islands
    :cvar XGZ: Gaza Strip
    :cvar XHO: Howland Island
    :cvar XJA: Johnston Atoll
    :cvar XJM: Jan Mayen
    :cvar XJN: Juan de Nova Island
    :cvar XJV: Jarvis Island
    :cvar XKM: Entity 4
    :cvar XKN: Entity 5
    :cvar XKR: Kingman Reef
    :cvar XKS: Republic of Kosovo
    :cvar XMW: Midway Islands
    :cvar XNV: Navassa Island
    :cvar XPL: Palmyra Atoll
    :cvar XPR: Paracel Islands
    :cvar XQZ: Akrotiri
    :cvar XSP: Spratly Islands
    :cvar XSV: Svalbard
    :cvar XTR: Tromelin Island
    :cvar XWB: West Bank
    :cvar XWK: Wake Island
    :cvar XXD: Dhekelia
    :cvar YEM: Republic of Yemen
    :cvar ZAF: Republic of South Africa
    :cvar ZMB: Republic of Zambia
    :cvar ZWE: Republic of Zimbabwe
    :cvar ACGU: FOUR EYES
    :cvar AMSP: AFRICOM Multinational Strategic Partners
    :cvar AOSC: Athens Olympics Security Coalition
    :cvar APFS: African Peacekeeping Force Somalia
    :cvar ASEA: Association of Southeast Asian Nations (ASEAN)
    :cvar AUSTRALIA_GROUP: Australia Group
    :cvar BHTF: Boko Haram Task Force
    :cvar BWCS: Biological Weapons Convention States
    :cvar CFCK: Combined Forces Command Korea
    :cvar CFOD: Coalition Forces Odyssey Dawn
    :cvar CFUP: Coalition Forces Unified Protector
    :cvar CLFC: Combined Libya Fusion Cell
    :cvar CMFC: Combined Maritime Forces Central
    :cvar CMFP: Cooperative Maritime Forces Pacific
    :cvar CPMT: Civilian Protection Monitoring Team for Sudan
    :cvar CTOC: Countering Transnational Organized Crime
    :cvar CWCS: Chemical Weapons Convention States
    :cvar ECTF: European Counter-Terrorism Forces
    :cvar EFOR: European Union Stabilization Forces in Bosnia
    :cvar EU: European Union
    :cvar EUDA: European Union DARFUR
    :cvar FRME: Counter Violent Extremist Organizations Framework
        Partners
    :cvar FVEY: FIVE EYES
    :cvar GCCH: Gulf Cooperation Council
    :cvar GCTF: Global Counter-Terrorism Forces
    :cvar GFNX: Global Foreign Terrorist Fighter Network Exchange
    :cvar GMIF: Global Maritime Interception Forces
    :cvar IESC: International Events Security Coalition
    :cvar IMSC: International Maritime Security Construct
    :cvar IMSP: INDOPACOM Multinational Strategic Partners
    :cvar IPMC: INDO PACIFIC Maritime Call
    :cvar IRKS: Inherent Resolve Kinetic Support
    :cvar ISAF: International Security Assistance Force for Afghanistan
    :cvar ISSG: International Syria Support Group
    :cvar KFOR: Stabilization Forces in Kosovo
    :cvar MCFI: Multinational Coalition Forces-Iraq
    :cvar MESF: Middle East Stability Force
    :cvar MGEU: Multinational GEOINT Europe
    :cvar MIFH: Multinational Interim Force Haiti
    :cvar MLEC: Multi-Lateral Enduring Contingency
    :cvar MNTF: Multinational Task Force
    :cvar MPFL: Multinational Peacekeeping Forces
    :cvar NACT: North African Counter-Terrorism Forces
    :cvar NATO: North Atlantic Treaty Organization
    :cvar NCFE: NATO CFE Treaty on Conventional Armed Forces in Europe
    :cvar NKIC: North Korea Intelligence Coalition
    :cvar NRDC: NORDIC
    :cvar NSG: Nuclear Suppliers' Group
    :cvar OSAG: Olympic Security Advisory Group
    :cvar OSTY: Open Skies Treaty
    :cvar PAWA: Partnership for Actions in West Africa
    :cvar PGMF: Persian Gulf Multinational Forces
    :cvar PSMX: Pacific Security Monitoring Exchange
    :cvar RISC: Russia Intelligence Sharing Coalition
    :cvar RSMA: Resolute Support Mission Afghanistan
    :cvar SFOR: Stabilization Force
    :cvar SOFP: Special Operations Forces Partners
    :cvar SPAA: SOF Planning Activities in Afghanistan (also called
        "11-Eyes")
    :cvar TEYE: THREE EYES
    :cvar TFTC: Terrorist Financing Targeting Center
    :cvar UNCK: United Nations Command, Korea
    """

    USA = "USA"
    ABW = "ABW"
    AFG = "AFG"
    AGO = "AGO"
    AIA = "AIA"
    ALB = "ALB"
    AND = "AND"
    ARE = "ARE"
    ARG = "ARG"
    ARM = "ARM"
    ASM = "ASM"
    ATA = "ATA"
    ATF = "ATF"
    ATG = "ATG"
    AUS = "AUS"
    AUT = "AUT"
    AX2 = "AX2"
    AX3 = "AX3"
    AZE = "AZE"
    BDI = "BDI"
    BEL = "BEL"
    BEN = "BEN"
    BES = "BES"
    BFA = "BFA"
    BGD = "BGD"
    BGR = "BGR"
    BHR = "BHR"
    BHS = "BHS"
    BIH = "BIH"
    BLM = "BLM"
    BLR = "BLR"
    BLZ = "BLZ"
    BMU = "BMU"
    BOL = "BOL"
    BRA = "BRA"
    BRB = "BRB"
    BRN = "BRN"
    BTN = "BTN"
    BVT = "BVT"
    BWA = "BWA"
    CAF = "CAF"
    CAN = "CAN"
    CCK = "CCK"
    CHE = "CHE"
    CHL = "CHL"
    CHN = "CHN"
    CIV = "CIV"
    CMR = "CMR"
    COD = "COD"
    COG = "COG"
    COK = "COK"
    COL = "COL"
    COM = "COM"
    CPT = "CPT"
    CPV = "CPV"
    CRI = "CRI"
    CUB = "CUB"
    CUW = "CUW"
    CXR = "CXR"
    CYM = "CYM"
    CYP = "CYP"
    CZE = "CZE"
    DEU = "DEU"
    DGA = "DGA"
    DJI = "DJI"
    DMA = "DMA"
    DNK = "DNK"
    DOM = "DOM"
    DZA = "DZA"
    ECU = "ECU"
    EGY = "EGY"
    ERI = "ERI"
    ESH = "ESH"
    ESP = "ESP"
    EST = "EST"
    ETH = "ETH"
    FIN = "FIN"
    FJI = "FJI"
    FLK = "FLK"
    FRA = "FRA"
    FRO = "FRO"
    FSM = "FSM"
    GAB = "GAB"
    GBR = "GBR"
    GEO = "GEO"
    GGY = "GGY"
    GHA = "GHA"
    GIB = "GIB"
    GIN = "GIN"
    GLP = "GLP"
    GMB = "GMB"
    GNB = "GNB"
    GNQ = "GNQ"
    GRC = "GRC"
    GRD = "GRD"
    GRL = "GRL"
    GTM = "GTM"
    GUF = "GUF"
    GUM = "GUM"
    GUY = "GUY"
    HKG = "HKG"
    HMD = "HMD"
    HND = "HND"
    HRV = "HRV"
    HTI = "HTI"
    HUN = "HUN"
    IDN = "IDN"
    IMN = "IMN"
    IND = "IND"
    IOT = "IOT"
    IRL = "IRL"
    IRN = "IRN"
    IRQ = "IRQ"
    ISL = "ISL"
    ISR = "ISR"
    ITA = "ITA"
    JAM = "JAM"
    JEY = "JEY"
    JOR = "JOR"
    JPN = "JPN"
    KAZ = "KAZ"
    KEN = "KEN"
    KGZ = "KGZ"
    KHM = "KHM"
    KIR = "KIR"
    KNA = "KNA"
    KOR = "KOR"
    KWT = "KWT"
    LAO = "LAO"
    LBN = "LBN"
    LBR = "LBR"
    LBY = "LBY"
    LCA = "LCA"
    LIE = "LIE"
    LKA = "LKA"
    LSO = "LSO"
    LTU = "LTU"
    LUX = "LUX"
    LVA = "LVA"
    MAC = "MAC"
    MAF = "MAF"
    MAR = "MAR"
    MCO = "MCO"
    MDA = "MDA"
    MDG = "MDG"
    MDV = "MDV"
    MEX = "MEX"
    MHL = "MHL"
    MKD = "MKD"
    MLI = "MLI"
    MLT = "MLT"
    MMR = "MMR"
    MNE = "MNE"
    MNG = "MNG"
    MNP = "MNP"
    MOZ = "MOZ"
    MRT = "MRT"
    MSR = "MSR"
    MTQ = "MTQ"
    MUS = "MUS"
    MWI = "MWI"
    MYS = "MYS"
    MYT = "MYT"
    NAM = "NAM"
    NCL = "NCL"
    NER = "NER"
    NFK = "NFK"
    NGA = "NGA"
    NIC = "NIC"
    NIU = "NIU"
    NLD = "NLD"
    NOR = "NOR"
    NPL = "NPL"
    NRU = "NRU"
    NZL = "NZL"
    OMN = "OMN"
    PAK = "PAK"
    PAN = "PAN"
    PCN = "PCN"
    PER = "PER"
    PHL = "PHL"
    PLW = "PLW"
    PNG = "PNG"
    POL = "POL"
    PRI = "PRI"
    PRK = "PRK"
    PRT = "PRT"
    PRY = "PRY"
    PYF = "PYF"
    QAT = "QAT"
    REU = "REU"
    ROU = "ROU"
    RUS = "RUS"
    RWA = "RWA"
    SAU = "SAU"
    SDN = "SDN"
    SEN = "SEN"
    SGP = "SGP"
    SGS = "SGS"
    SHN = "SHN"
    SLB = "SLB"
    SLE = "SLE"
    SLV = "SLV"
    SMR = "SMR"
    SOM = "SOM"
    SPM = "SPM"
    SRB = "SRB"
    SSD = "SSD"
    STP = "STP"
    SUR = "SUR"
    SVK = "SVK"
    SVN = "SVN"
    SWE = "SWE"
    SWZ = "SWZ"
    SXM = "SXM"
    SYC = "SYC"
    SYR = "SYR"
    TCA = "TCA"
    TCD = "TCD"
    TGO = "TGO"
    THA = "THA"
    TJK = "TJK"
    TKL = "TKL"
    TKM = "TKM"
    TLS = "TLS"
    TON = "TON"
    TTO = "TTO"
    TUN = "TUN"
    TUR = "TUR"
    TUV = "TUV"
    TWN = "TWN"
    TZA = "TZA"
    UGA = "UGA"
    UKR = "UKR"
    URY = "URY"
    UZB = "UZB"
    VAT = "VAT"
    VCT = "VCT"
    VEN = "VEN"
    VGB = "VGB"
    VIR = "VIR"
    VNM = "VNM"
    VUT = "VUT"
    WLF = "WLF"
    WSM = "WSM"
    XAC = "XAC"
    XAZ = "XAZ"
    XBI = "XBI"
    XBK = "XBK"
    XCR = "XCR"
    XCS = "XCS"
    XCY = "XCY"
    XEU = "XEU"
    XGL = "XGL"
    XGZ = "XGZ"
    XHO = "XHO"
    XJA = "XJA"
    XJM = "XJM"
    XJN = "XJN"
    XJV = "XJV"
    XKM = "XKM"
    XKN = "XKN"
    XKR = "XKR"
    XKS = "XKS"
    XMW = "XMW"
    XNV = "XNV"
    XPL = "XPL"
    XPR = "XPR"
    XQZ = "XQZ"
    XSP = "XSP"
    XSV = "XSV"
    XTR = "XTR"
    XWB = "XWB"
    XWK = "XWK"
    XXD = "XXD"
    YEM = "YEM"
    ZAF = "ZAF"
    ZMB = "ZMB"
    ZWE = "ZWE"
    ACGU = "ACGU"
    AMSP = "AMSP"
    AOSC = "AOSC"
    APFS = "APFS"
    ASEA = "ASEA"
    AUSTRALIA_GROUP = "AUSTRALIA_GROUP"
    BHTF = "BHTF"
    BWCS = "BWCS"
    CFCK = "CFCK"
    CFOD = "CFOD"
    CFUP = "CFUP"
    CLFC = "CLFC"
    CMFC = "CMFC"
    CMFP = "CMFP"
    CPMT = "CPMT"
    CTOC = "CTOC"
    CWCS = "CWCS"
    ECTF = "ECTF"
    EFOR = "EFOR"
    EU = "EU"
    EUDA = "EUDA"
    FRME = "FRME"
    FVEY = "FVEY"
    GCCH = "GCCH"
    GCTF = "GCTF"
    GFNX = "GFNX"
    GMIF = "GMIF"
    IESC = "IESC"
    IMSC = "IMSC"
    IMSP = "IMSP"
    IPMC = "IPMC"
    IRKS = "IRKS"
    ISAF = "ISAF"
    ISSG = "ISSG"
    KFOR = "KFOR"
    MCFI = "MCFI"
    MESF = "MESF"
    MGEU = "MGEU"
    MIFH = "MIFH"
    MLEC = "MLEC"
    MNTF = "MNTF"
    MPFL = "MPFL"
    NACT = "NACT"
    NATO = "NATO"
    NCFE = "NCFE"
    NKIC = "NKIC"
    NRDC = "NRDC"
    NSG = "NSG"
    OSAG = "OSAG"
    OSTY = "OSTY"
    PAWA = "PAWA"
    PGMF = "PGMF"
    PSMX = "PSMX"
    RISC = "RISC"
    RSMA = "RSMA"
    SFOR = "SFOR"
    SOFP = "SOFP"
    SPAA = "SPAA"
    TEYE = "TEYE"
    TFTC = "TFTC"
    UNCK = "UNCK"


class SciControlsEnum(Enum):
    """
    CVEnumISMSCIControls Values.

    :cvar BUR: BUR
    :cvar BUR_BLG: BUR-BLG
    :cvar BUR_DTP: BUR-DTP
    :cvar BUR_WRG: BUR-WRG
    :cvar HCS: HCS
    :cvar HCS_O: HCS-O
    :cvar HCS_P: HCS-P
    :cvar HCS_X: HCS-X
    :cvar KLM: KLAMATH
    :cvar KLM_R: KLAMATH-R
    :cvar MVL: MARVEL
    :cvar RSV: RESERVE
    :cvar SI: SPECIAL INTELLIGENCE
    :cvar SI_EU: ECRU
    :cvar SI_G: SI-GAMMA
    :cvar SI_NK: NONBOOK
    :cvar TK: TALENT KEYHOLE
    :cvar TK_BLFH: BLUEFISH
    :cvar TK_IDIT: IDITAROD
    :cvar TK_KAND: KANDIK
    """

    BUR = "BUR"
    BUR_BLG = "BUR_BLG"
    BUR_DTP = "BUR_DTP"
    BUR_WRG = "BUR_WRG"
    HCS = "HCS"
    HCS_O = "HCS_O"
    HCS_P = "HCS_P"
    HCS_X = "HCS_X"
    KLM = "KLM"
    KLM_R = "KLM_R"
    MVL = "MVL"
    RSV = "RSV"
    SI = "SI"
    SI_EU = "SI_EU"
    SI_G = "SI_G"
    SI_NK = "SI_NK"
    TK = "TK"
    TK_BLFH = "TK_BLFH"
    TK_IDIT = "TK_IDIT"
    TK_KAND = "TK_KAND"


class SecondBannerLineEnum(Enum):
    """
    (U) All currently valid markings that can appear in the second banner
    line.

    This enum is used by SecondBannerLine. PERMISSIBLE VALUES The
    permissible values for this simple type are defined in the Controlled
    Value Enumeration: CVEnumISMSecondBannerLine.xml.

    :cvar ACPI: ATTORNEY-CLIENT PRIVILEGED INFO
    :cvar AWP: ATTORNEY WORK PRODUCT
    :cvar CUSPI: CONTENTS INCLUDE US PERSON INFORMATION
    :cvar DPPD: DELIBERATIVE PROCESS PRIVILEGED DOCUMENT
    :cvar HVCO: HANDLE VIA CHANNELS ONLY
    :cvar SSS: SOURCE SELECTION SENSITIVE
    """

    ACPI = "ACPI"
    AWP = "AWP"
    CUSPI = "CUSPI"
    DPPD = "DPPD"
    HVCO = "HVCO"
    SSS = "SSS"


@dataclass(kw_only=True)
class FgiSourceOpenChoiceType:
    """
    Encoding types for CVEnumISMCATFGIOpen Version 2 controlled vocabulary
    enumerations.

    Derived from the CVEnumISMCATFGIOpen.xml CVE. (U) All currently valid
    GENC trigraphs except USA in alphabetical order by trigraph, followed
    by all currently valid CAPCO Coalition tetragraphs in alphabetical
    order by tetragraph. UNKNOWN removed since GENC has it as AX1
    PERMISSIBLE VALUES The permissible values for this simple type are
    defined in the Controlled Value Enumeration: CVEnumISMCATFGIOpen.xml.

    :ivar foreign_government_identifier: CVEnumISMCATFGIOpen Values
    :ivar nato_special_word: North Atlantic Treaty Organization Special
        Words
    """

    class Meta:
        name = "FGI_SourceOpenChoiceType"

    foreign_government_identifier: None | FgiSourceOpenEnum = field(
        default=None,
        metadata={
            "name": "ForeignGovernmentIdentifier",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        },
    )
    nato_special_word: None | str = field(
        default=None,
        metadata={
            "name": "NATO_SpecialWord",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 6,
            "max_length": 261,
            "pattern": r"NATO:[a-zA-Z\-_]{1,256}",
        },
    )


@dataclass(kw_only=True)
class FgiSourceProtectedChoiceType:
    """
    Encoding types for CVEnumISMCATFGIProtected Version 2.1 controlled
    vocabulary enumerations.

    Derived from the CVEnumISMCATFGIProtected.xml CVE. (U) FGI, followed by
    GENC trigraphs (except USA and AX1) in alphabetical order by trigraph,
    followed by IC Markings System Register and Manual Coalition
    tetragraphs in alphabetical order by tetragraph. PERMISSIBLE VALUES The
    permissible values for this simple type are defined in the Controlled
    Value Enumeration: CVEnumISMCATFGIProtected.xml.

    :ivar foreign_government_identifier: CVEnumISMCATFGIProtected Values
    :ivar nato_special_word: North Atlantic Treaty Organization Special
        Words
    """

    class Meta:
        name = "FGI_SourceProtectedChoiceType"

    foreign_government_identifier: None | FgiSourceProtectedEnum = field(
        default=None,
        metadata={
            "name": "ForeignGovernmentIdentifier",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        },
    )
    nato_special_word: None | str = field(
        default=None,
        metadata={
            "name": "NATO_SpecialWord",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 6,
            "max_length": 261,
            "pattern": r"NATO:[a-zA-Z\-_]{1,256}",
        },
    )


@dataclass(kw_only=True)
class OwnerProducerChoiceType:
    """
    Encoding types for CVEnumISMCATOwnerProducer Version 2 controlled
    vocabulary enumerations.

    Derived from the CVEnumISMCATOwnerProducer.xml CVE. (U) FGI, followed
    by all currently valid GENC trigraphs in alphabetical order by
    trigraph, followed by all currently valid CAPCO Coalition tetragraphs
    in alphabetical order by tetragraph. PERMISSIBLE VALUES The permissible
    values for this simple type are defined in the Controlled Value
    Enumeration: CVEnumISMCATOwnerProducer.xml.

    :ivar government_identifier: CVEnumISMCATOwnerProducer Values
    :ivar nato_special_word: North Atlantic Treaty Organization Special
        Words
    """

    government_identifier: None | OwnerProducerEnum = field(
        default=None,
        metadata={
            "name": "GovernmentIdentifier",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        },
    )
    nato_special_word: None | str = field(
        default=None,
        metadata={
            "name": "NATO_SpecialWord",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 6,
            "max_length": 261,
            "pattern": r"NATO:[a-zA-Z\-_]{1,256}",
        },
    )


@dataclass(kw_only=True)
class ReleasableToChoiceType:
    """
    Encoding types for CVEnumISMCATRelTo Version 2 controlled vocabulary
    enumerations.

    Derived from the CVEnumISMCATRelTo.xml CVE. (U) USA, followed by all
    currently valid GENC trigraphs except USA in alphabetical order by
    trigraph, followed by all currently valid CAPCO Coalition tetragraphs
    in alphabetical order by tetragraph. PERMISSIBLE VALUES The permissible
    values for this simple type are defined in the Controlled Value
    Enumeration: CVEnumISMCATRelTo.xml.

    :ivar government_identifier: CVEnumISMCATRelTo Values
    :ivar nato_special_word: North Atlantic Treaty Organization Special
        Words
    """

    government_identifier: None | ReleasableToEnum = field(
        default=None,
        metadata={
            "name": "GovernmentIdentifier",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        },
    )
    nato_special_word: None | str = field(
        default=None,
        metadata={
            "name": "NATO_SpecialWord",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 6,
            "max_length": 261,
            "pattern": r"NATO:[a-zA-Z\-_]{1,256}",
        },
    )


@dataclass(kw_only=True)
class SecurityInformationType:
    """
    This type indicates a variety of security information for a data asset
    including how a data asset shall be stored, protected, and destroyed.

    This type is based on IC ISM SecurityAttributesGroup IC-ISM.xsd.

    :ivar classification: A single indicator of the highest level of
        classification applicable to an information resource or portion
        within the domain of classified national security information.
    :ivar owner_producer: Identifies the national government or
        international organization that have purview over the
        classification marking of an information resource or portion
        therein. Within protected internal organizational spaces this
        element may include up to 1000 indicators identifying
        information which qualifies as foreign government information
        for which the source(s) of the information must be concealed.
        Measures must be taken prior to dissemination of the information
        to conceal the source(s) of the foreign government information.
        Specifically, under these specific circumstances, when data are
        moved to the shared spaces, the non-disclosable owner(s) and/or
        producer(s) listed in this data element's value should be
        removed and replaced with "FGI".
    :ivar joint: When true, is used to signify that multiple values in
        the OwnerProducer element are JOINT owners of the data.
    :ivar sci_controls: Identifies sensitive compartmented information
        control system(s). List size for this element is based on
        "Select All That Apply" condition.
    :ivar sar_identifier: Identifies the defense or intelligence
        programs for which special access is required.
    :ivar atomic_energy_markings: Identifies DoE markings. List size for
        this element is based on "Select All That Apply" condition.
    :ivar dissemination_controls: Identifies the expansion or limitation
        on the distribution of information. List size for this element
        is based on "Select All That Apply" condition.
    :ivar display_only_to: Identifies the country/countries and/or
        international organization(s) to which classified information
        may be displayed but NOT released based on the determination of
        an originator in accordance with established foreign disclosure
        procedures. This element is used in conjunction with the
        DisplayOnly Dissemination Controls value.
    :ivar fgi_source_open: Identifies information which qualifies as
        foreign government information for which the source(s) of the
        information is not concealed. The attribute can indicate that
        the source of information of foreign origin is UNKNOWN.
    :ivar fgi_source_protected: Identifies information which qualifies
        as foreign government information for which the source(s) of the
        information must be concealed. The attribute can indicate that
        the source of information of foreign origin is UNKNOWN.
    :ivar releasable_to: Identifies the country or countries and/or
        international organization(s) to which classified information
        may be released based on the determination of an originator in
        accordance with established foreign disclosure procedures. This
        element is used in conjunction with the Dissemination Controls
        element.
    :ivar non_ic_markings: Identifies the expansion or limitation on the
        distribution of an information resource or portion within the
        domain of information originating from non-intelligence
        components. List size for this element is based on "Select All
        That Apply" condition.
    :ivar classified_by: Identifies, by name or personal identifier, and
        position title of the original classification authority for a
        resource.
    :ivar compilation_reason: A description of the reasons that the
        classification of this element is more restrictive than a simple
        roll-up of the sub elements would result in. This acts as an
        indicator to rule engines that there is not accidental over
        classification going on and to users that special care beyond
        what the portion marks reveal must be taken when using this
        data. Use of this mark does not replace the need for the
        compilation reason being defined in the prose in accordance with
        ISOO Directive 1. For example this would document why 3
        Unclassified bullet items form a Secret List. Without this
        reason being noted the above described document would be
        considered to be miss-marked and overclassified.
    :ivar derivatively_classified_by: Identifies, by name or personal
        identifier, of the derivative classification authority.
    :ivar classification_reason: This element is used primarily at the
        resource level. One or more reason indicators or explanatory
        text describing the basis for an original classification
        decision. It is manifested only in the 'Reason' line of a
        resource's classification authority block.
    :ivar non_us_controls: One or more indicators of the expansion or
        limitation on the distribution of an information resource or
        portion within the domain of information originating from non-US
        components. List size for this element is based on "Select All
        That Apply" condition.
    :ivar derived_from: A citation of the authoritative source or
        reference to multiple sources of the classification markings
        used in a classified resource. It is manifested only in the
        'Derived From' line of a document's classification authority
        block. ISOO's guidance is: Source of derivative classification.
        (1) The derivative classifier shall concisely identify the
        source document or the classification guide on the "Derived
        From" line, including the agency and, where available, the
        office of origin, and the date of the source or guide. An
        example might appear as: Derived From: Memo, "Funding Problems,"
        October 20, 2008, Office of Administration, Department of Good
        Works or Derived From: CG No. 1, Department of Good Works, dated
        October 20, 2008 (i) When a document is classified derivatively
        on the basis of more than one source document or classification
        guide, the "Derived From" line shall appear as: Derived From:
        Multiple Sources (ii) The derivative classifier shall include a
        listing of the source materials on, or attached to, each
        derivatively classified document.
    :ivar declass_date: A specific year, month, and day upon which the
        information shall be automatically declassified if not properly
        exempted from automatic declassification.
    :ivar declass_event: A description of an event upon which the
        information shall be automatically declassified if not properly
        exempted from automatic declassification.
    :ivar declass_exception: A single indicator describing an exemption
        to the nominal 25-year point for automatic declassification.
        This element is used in conjunction with the Declassification
        Date or Declassification Event. ISOO has stated it should be a
        SINGLE value giving the longest protection. List size for this
        element is based on "Select All That Apply" condition.
    :ivar has_approximate_markings: When true, indicates the ISM
        markings specified are estimated (e.g., system high).
    :ivar high_water_nato: Applicable NATO highwater markings for a
        document or portion. List size for this element is based on
        "Select All That Apply" condition.
    :ivar cui_basic: Applicable CUI Basic markings for a document or
        portion. List size for this element is based on "Select All That
        Apply" condition.
    :ivar cui_specified: Applicable CUI Specified markings for a
        document or portion. List size for this element is based on
        "Select All That Apply" condition.
    :ivar cui_decontrol_date: The specific date when a CUI resource is
        subject to automatic CUI decontrol procedures.
    :ivar cui_decontrol_event: A description of an event upon which CUI
        information shall be subject to automatic decontrol procedures.
    :ivar cui_controlled_by: The identity, by name or personal
        identifier and position title, of the CUI controlling authority
        for a document containing CUI information.
    :ivar cui_controlled_by_office: Office in an agency or department
        that is responsible for labeling and controlling information as
        CUI.
    :ivar cui_poc: Point of Contact for labeling and controlling
        information as CUI.
    :ivar second_banner_line: Tokens that contain markings used to
        support administrative and legal processes for handling and
        protecting documents. When they appear in a document, these
        tokens form a second line that is placed below the banner. List
        size for this element is based on "Select All That Apply"
        condition.
    :ivar handle_via_channels: Handle VIA Channels that may appear in
        the second banner line.
    """

    classification: ClassificationEnum = field(
        metadata={
            "name": "Classification",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        }
    )
    owner_producer: list[OwnerProducerChoiceType] = field(
        default_factory=list,
        metadata={
            "name": "OwnerProducer",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_occurs": 1,
        },
    )
    joint: None | bool = field(
        default=None,
        metadata={
            "name": "Joint",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        },
    )
    sci_controls: list[SciControlsEnum] = field(
        default_factory=list,
        metadata={
            "name": "SCI_Controls",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "max_occurs": 20,
        },
    )
    sar_identifier: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SAR_Identifier",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 0,
            "max_length": 4096,
            "white_space": "collapse",
            "pattern": r"[ -~\n\r]{0,4096}",
        },
    )
    atomic_energy_markings: list[AtomicEnergyMarkingsEnum] = field(
        default_factory=list,
        metadata={
            "name": "AtomicEnergyMarkings",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "max_occurs": 14,
        },
    )
    dissemination_controls: list[DisseminationControlsEnum] = field(
        default_factory=list,
        metadata={
            "name": "DisseminationControls",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "max_occurs": 22,
        },
    )
    display_only_to: list[ReleasableToChoiceType] = field(
        default_factory=list,
        metadata={
            "name": "DisplayOnlyTo",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        },
    )
    fgi_source_open: list[FgiSourceOpenChoiceType] = field(
        default_factory=list,
        metadata={
            "name": "FGI_SourceOpen",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        },
    )
    fgi_source_protected: list[FgiSourceProtectedChoiceType] = field(
        default_factory=list,
        metadata={
            "name": "FGI_SourceProtected",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        },
    )
    releasable_to: list[ReleasableToChoiceType] = field(
        default_factory=list,
        metadata={
            "name": "ReleasableTo",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        },
    )
    non_ic_markings: list[NonIcMarkingsEnum] = field(
        default_factory=list,
        metadata={
            "name": "NonIC_Markings",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "max_occurs": 9,
        },
    )
    classified_by: None | str = field(
        default=None,
        metadata={
            "name": "ClassifiedBy",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 0,
            "max_length": 1024,
            "white_space": "collapse",
            "pattern": r"[ -~\n\r]{0,1024}",
        },
    )
    compilation_reason: None | str = field(
        default=None,
        metadata={
            "name": "CompilationReason",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 0,
            "max_length": 1024,
            "white_space": "collapse",
            "pattern": r"[ -~\n\r]{0,1024}",
        },
    )
    derivatively_classified_by: None | str = field(
        default=None,
        metadata={
            "name": "DerivativelyClassifiedBy",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 0,
            "max_length": 1024,
            "white_space": "collapse",
            "pattern": r"[ -~\n\r]{0,1024}",
        },
    )
    classification_reason: None | str = field(
        default=None,
        metadata={
            "name": "ClassificationReason",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 0,
            "max_length": 4096,
            "white_space": "collapse",
            "pattern": r"[ -~\n\r]{0,4096}",
        },
    )
    non_us_controls: list[NonUsControlsEnum] = field(
        default_factory=list,
        metadata={
            "name": "NonUS_Controls",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "max_occurs": 3,
        },
    )
    derived_from: None | str = field(
        default=None,
        metadata={
            "name": "DerivedFrom",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 0,
            "max_length": 1024,
            "white_space": "collapse",
            "pattern": r"[ -~\n\r]{0,1024}",
        },
    )
    declass_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "DeclassDate",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        },
    )
    declass_event: None | str = field(
        default=None,
        metadata={
            "name": "DeclassEvent",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 0,
            "max_length": 1024,
            "white_space": "collapse",
            "pattern": r"[ -~\n\r]{0,1024}",
        },
    )
    declass_exception: list[DeclassExceptionEnum] = field(
        default_factory=list,
        metadata={
            "name": "DeclassException",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "max_occurs": 25,
        },
    )
    has_approximate_markings: None | bool = field(
        default=None,
        metadata={
            "name": "HasApproximateMarkings",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        },
    )
    high_water_nato: list[HighWaterNatoEnum] = field(
        default_factory=list,
        metadata={
            "name": "HighWaterNATO",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "max_occurs": 5,
        },
    )
    cui_basic: list[CuiBasicEnum] = field(
        default_factory=list,
        metadata={
            "name": "CUI_Basic",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "max_occurs": 93,
        },
    )
    cui_specified: list[CuiSpecifiedEnum] = field(
        default_factory=list,
        metadata={
            "name": "CUI_Specified",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "max_occurs": 57,
        },
    )
    cui_decontrol_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "CUI_DecontrolDate",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
        },
    )
    cui_decontrol_event: None | str = field(
        default=None,
        metadata={
            "name": "CUI_DecontrolEvent",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 0,
            "max_length": 1024,
            "white_space": "collapse",
            "pattern": r"[ -~\n\r]{0,1024}",
        },
    )
    cui_controlled_by: None | str = field(
        default=None,
        metadata={
            "name": "CUI_ControlledBy",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 0,
            "max_length": 1024,
            "white_space": "collapse",
            "pattern": r"[ -~\n\r]{0,1024}",
        },
    )
    cui_controlled_by_office: None | str = field(
        default=None,
        metadata={
            "name": "CUI_ControlledByOffice",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 0,
            "max_length": 1024,
            "white_space": "collapse",
            "pattern": r"[ -~\n\r]{0,1024}",
        },
    )
    cui_poc: None | str = field(
        default=None,
        metadata={
            "name": "CUI_POC",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 0,
            "max_length": 1024,
            "white_space": "collapse",
            "pattern": r"[ -~\n\r]{0,1024}",
        },
    )
    second_banner_line: list[SecondBannerLineEnum] = field(
        default_factory=list,
        metadata={
            "name": "SecondBannerLine",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "max_occurs": 6,
        },
    )
    handle_via_channels: None | str = field(
        default=None,
        metadata={
            "name": "HandleViaChannels",
            "type": "Element",
            "namespace": "https://www.vdl.afrl.af.mil/programs/oam",
            "min_length": 0,
            "max_length": 4096,
            "white_space": "collapse",
            "pattern": r"[ -~\n\r]{0,4096}",
        },
    )
